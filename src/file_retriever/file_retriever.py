from typing import List

from src.repository_client.github_client import GithubClient
from src.utils.logger import Logger


class FileRetriever:
    def __init__(self, repository_client: GithubClient, file_extension: str):
        self.repository_client = repository_client
        self.file_extension = file_extension
        self.logger = Logger().get_logger()

    def get_files(self, username: str, repository_name: str, max_files: int, path: str = '') -> List[str]:
        directory_contents = self.repository_client.get_directory_contents(username, repository_name, path)

        if directory_contents is None:
            return []

        files = []
        for item in directory_contents:
            if len(files) >= max_files:
                break

            if item['type'] == 'dir':
                self.logger.info(f"Exploring directory: {item['path']}")
                subdir_files = self.get_files(username, repository_name, max_files - len(files), item['path'])
                files.extend(subdir_files)
            elif item['path'].endswith(self.file_extension):
                files.append(item['path'])

        self.logger.info(f"Found {len(files)} {self.file_extension} files in {path}")
        return files
