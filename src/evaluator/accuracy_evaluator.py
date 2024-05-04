import random
import torch
from torch.utils.data import DataLoader, pad_sequence
from tqdm import tqdm


class AccuracyEvaluator:
    def __init__(self, model, tokenizer, test_dataset, mask_ratio=0.15, num_samples=2, batch_size=16):
        self.model = model
        self.tokenizer = tokenizer
        self.test_dataset = test_dataset
        self.mask_ratio = mask_ratio
        self.num_samples = num_samples
        self.batch_size = batch_size
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def evaluate_accuracy(self):
            accuracies = []
            test_dataloader = DataLoader(self.test_dataset, batch_size=self.batch_size)

            padding_value = self.tokenizer.pad_token_id if self.tokenizer.pad_token_id is not None else 0

            for batch in tqdm(test_dataloader):
                input_ids_batch = batch["input_ids"]
                max_length = max(len(input_ids) for input_ids in input_ids_batch)

                masked_input_ids_batch = []

                for input_ids in input_ids_batch:
                    input_ids = torch.tensor(input_ids)
                    for _ in range(self.num_samples):
                        mask_index = random.randint(0, len(input_ids) - 1)
                        masked_input_ids = input_ids[:mask_index].clone().detach()

                        masked_input_ids_batch.append(masked_input_ids)

                masked_input_ids_batch = pad_sequence(masked_input_ids_batch, batch_first=True, padding_value=padding_value).to(self.device)

                with torch.no_grad():
                    outputs = self.model.generate(
                        input_ids=masked_input_ids_batch,
                        max_length=max_length,
                        num_return_sequences=1,
                        pad_token_id=self.tokenizer.pad_token_id
                    )

                    for i in range(len(input_ids_batch)):
                        for j in range(self.num_samples):
                            output_index = i * self.num_samples + j
                            predicted_ids = outputs[output_index][len(masked_input_ids_batch[output_index]):].cpu()
                            input_ids = input_ids_batch[i]
                            accuracy = (predicted_ids == input_ids).float().mean().item()
                            accuracies.append(accuracy)

            return sum(accuracies) / len(accuracies)
