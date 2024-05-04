import torch
from tqdm import tqdm


class PerplexityEvaluator:
    def __init__(self, model, tokenizer, test_dataset):
        self.model = model
        self.tokenizer = tokenizer
        self.test_dataset = test_dataset
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def evaluate_perplexity(self):
        max_length = 512  # Set the maximum sequence length manually
        stride = 512
        nlls = []

        for example in tqdm(self.test_dataset):
            input_ids = example["input_ids"]
            seq_len = len(input_ids)

            prev_end_loc = 0
            for begin_loc in range(0, seq_len, stride):
                end_loc = min(begin_loc + max_length, seq_len)
                trg_len = end_loc - prev_end_loc

                input_ids_batch = torch.tensor(input_ids[begin_loc:end_loc]).unsqueeze(0).to(self.device)
                target_ids_batch = input_ids_batch.clone()
                target_ids_batch[:, :-trg_len] = -100

                with torch.no_grad():
                    outputs = self.model(input_ids_batch, labels=target_ids_batch)
                    neg_log_likelihood = outputs.loss
                    nlls.append(neg_log_likelihood)

                prev_end_loc = end_loc
                if end_loc == seq_len:
                    break

        ppl = torch.exp(torch.stack(nlls).mean())
        return ppl
