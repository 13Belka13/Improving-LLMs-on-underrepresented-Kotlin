from enum import Enum
from src.code_preprocessor.kotlin_code_preprocessor import KotlinCodePreprocessor
from src.code_preprocessor.python_code_preprocessor import PythonCodePreprocessor
from src.data.dataset_generator import DatasetGenerator
from src.file_retriever.file_retriever import FileRetriever
from src.repository_client.github_client import GithubClient
from src.utils.env_loader import GITHUB_TOKEN
from src.utils.logger import Logger


class LanguageType(Enum):
    PYTHON = "Python"
    KOTLIN = "Kotlin"


def generate_dataset(
        language: LanguageType,
        repo_username: str,
        repo_name: str,
        max_files: int,
        output_file: str,
        file_extension: str,
):

    logger = Logger().get_logger()

    logger.info(f"Generating {language} dataset")
    github_client = GithubClient(GITHUB_TOKEN)
    file_retriever = FileRetriever(github_client, file_extension)

    if language == LanguageType.PYTHON:
        code_preprocessor = PythonCodePreprocessor()
    elif language == LanguageType.KOTLIN:
        code_preprocessor = KotlinCodePreprocessor()
    else:
        raise ValueError(f"Unsupported language: {language}")

    dataset_generator = DatasetGenerator(file_retriever, code_preprocessor)
    dataset_generator.generate_dataset(repo_username, repo_name, max_files, output_file)
    logger.info(f"{language.value} dataset generation completed")
