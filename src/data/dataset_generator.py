import base64

from tqdm import tqdm

from src.code_preprocessor.base import CodePreprocessor
from src.file_retriever.file_retriever import FileRetriever
from src.utils.logger import Logger


class DatasetGenerator:
    def __init__(self, file_retriever: FileRetriever, preprocessor: CodePreprocessor):
        self.file_retriever = file_retriever
        self.preprocessor = preprocessor
        self.logger = Logger().get_logger()

    def generate_dataset(self, username: str, repository_name: str, max_files: int, output_file: str):
        self.logger.info(f"Generating dataset from {username}/{repository_name}")
        files = self.file_retriever.get_files(username, repository_name, max_files)

        with open(output_file, 'w', encoding='utf-8') as file:
            for file_path in tqdm(files, desc="Processing files"):
                file_content = self.file_retriever.repository_client.get_file_content(username, repository_name, file_path)
                if file_content is not None:
                    decoded_content = base64.b64decode(file_content['content']).decode('utf-8')
                    preprocessed_code = self.preprocessor.preprocess_code(decoded_content)
                    file.write(preprocessed_code + '\n')
                else:
                    self.logger.warning(f"Skipping file {file_path} due to reading error")

        self.logger.info(f"Dataset generated and saved to {output_file}")
