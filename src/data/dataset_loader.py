from datasets import load_dataset


class DatasetLoader:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

    def load_dataset(self):
        data = load_dataset("text", data_files=self.dataset_path)
        return data["train"]
