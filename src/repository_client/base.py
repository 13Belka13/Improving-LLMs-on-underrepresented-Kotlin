from abc import ABC, abstractmethod
from typing import Dict, Optional


class RepositoryClient(ABC):
    @abstractmethod
    def get_file_content(self, username: str, repository_name: str, file_path: str) -> Optional[str]:
        pass

    @abstractmethod
    def get_directory_contents(self, username: str, repository_name: str, directory_path: str) -> Optional[Dict]:
        pass
