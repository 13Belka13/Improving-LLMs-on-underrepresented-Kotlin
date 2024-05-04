from sklearn.model_selection import train_test_split


class DatasetSplitter:
    def __init__(self, dataset, test_size=0.2, random_state=42):
        self.dataset = dataset
        self.test_size = test_size
        self.random_state = random_state

    def split_dataset(self):
        train_data, test_data = train_test_split(self.dataset, test_size=self.test_size, random_state=self.random_state)
        return train_data, test_data
