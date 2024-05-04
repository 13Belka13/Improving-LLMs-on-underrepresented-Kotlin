from abc import ABC, abstractmethod
from typing import Dict, List
import re

from src.utils.logger import Logger


class CodePreprocessor(ABC):
    def __init__(self):
        self.logger = Logger().get_logger()
        self.replacement_patterns: Dict[re.Pattern, str] = {}

    def _replace_patterns(self, code: str) -> str:
        for pattern, replacement in self.replacement_patterns.items():
            code = pattern.sub(replacement, code)
        return code

    @abstractmethod
    def _tokenize(self, code: str) -> List[str]:
        pass

    @abstractmethod
    def _normalize_identifiers(self, tokens: List[str]) -> List[str]:
        pass

    def preprocess_code(self, code: str) -> str:
        try:
            code = self._replace_patterns(code)
            tokens = self._tokenize(code)
            tokens = [token for token in tokens if not token.isspace()]
            normalized_tokens = self._normalize_identifiers(tokens)
            preprocessed_code = ['<start>'] + normalized_tokens + ['<end>']
            return ' '.join(preprocessed_code)
        except Exception as e:
            self.logger.error(f"Error preprocessing code: {str(e)}")
            return ''
