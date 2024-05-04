from typing import Optional, Dict

import requests

from src.repository_client.base import RepositoryClient
from src.utils.logger import Logger


class GithubClient(RepositoryClient):
    def __init__(self, github_token: Optional[str] = None):
        self.base_url = 'https://api.github.com'
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        if github_token:
            self.headers['Authorization'] = f'token {github_token}'

        self.logger = Logger().get_logger()

    def _request(self, url: str) -> Optional[Dict]:
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f'Error occurred while making request: {url}')
            self.logger.error(str(e))
            return None

    def get_file_content(self, username: str, repository_name: str, file_path: str) -> Optional[str]:
        url = f'{self.base_url}/repos/{username}/{repository_name}/contents/{file_path}'
        return self._request(url)

    def get_directory_contents(self, username: str, repository_name: str, directory_path: str) -> Optional[Dict]:
        url = f'{self.base_url}/repos/{username}/{repository_name}/contents/{directory_path}'
        return self._request(url)
