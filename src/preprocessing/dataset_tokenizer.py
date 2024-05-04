from datasets import Dataset


class DatasetTokenizer:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def tokenize_function(self, examples):
        return self.tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

    def prepare_dataset(self, dataset):
        dataset = Dataset.from_dict(dataset)
        tokenized_dataset = dataset.map(self.tokenize_function, batched=True, remove_columns=dataset.column_names)
        return tokenized_dataset