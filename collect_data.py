from typing import List
from src.utils.env_loader import (
    KOTLIN_REPO_USERNAME,
    KOTLIN_REPO_NAME,
    KOTLIN_MAX_FILES,
    KOTLIN_OUTPUT_FILE,
    PYTHON_REPO_USERNAME,
    PYTHON_REPO_NAME,
    PYTHON_MAX_FILES,
    PYTHON_OUTPUT_FILE,
)
from src.utils.generate_dataset import LanguageType, generate_dataset
from src.utils.logger import Logger


def main():
    logger = Logger().get_logger()

    logger.info("Starting dataset generation")

    generate_configs: List[dict] = [
        {
            "language": LanguageType.PYTHON,
            "repo_username": PYTHON_REPO_USERNAME,
            "repo_name": PYTHON_REPO_NAME,
            "max_files": PYTHON_MAX_FILES,
            "output_file": PYTHON_OUTPUT_FILE,
            "file_extension": ".py",
        },
        {
            "language": LanguageType.KOTLIN,
            "repo_username": KOTLIN_REPO_USERNAME,
            "repo_name": KOTLIN_REPO_NAME,
            "max_files": KOTLIN_MAX_FILES,
            "output_file": KOTLIN_OUTPUT_FILE,
            "file_extension": ".kt",
        },
    ]

    for config in generate_configs:
        generate_dataset(**config)

    logger.info("Dataset generation completed")


if __name__ == "__main__":
    main()
