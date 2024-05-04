import re
from typing import Dict, List

from src.code_preprocessor.base import CodePreprocessor
from src.utils.logger import Logger

from src.constants.kotlin_constants import BUILT_IN_FUNCTIONS, KEYWORD_DICT
from src.constants.kotlin_patterns import (
    TOKEN_PATTERN, COMMENT_PATTERN, IMPORT_PATTERN, PACKAGE_PATTERN,
    STRING_LITERAL_PATTERN, NUMBER_LITERAL_PATTERN, ANNOTATION_PATTERN
)


class KotlinCodePreprocessor(CodePreprocessor):
    def __init__(self):
        super().__init__()
        self.replacement_patterns: Dict[re.Pattern, str] = {
            COMMENT_PATTERN: '',
            IMPORT_PATTERN: '',
            PACKAGE_PATTERN: '',
            STRING_LITERAL_PATTERN: 'STRING_LITERAL',
            NUMBER_LITERAL_PATTERN: 'LITERAL'
        }

        self.token_pattern = TOKEN_PATTERN
        self.annotation_pattern = ANNOTATION_PATTERN

        self.built_in_functions = BUILT_IN_FUNCTIONS
        self.keyword_dict = KEYWORD_DICT

        self.logger = Logger().get_logger()

    def _tokenize(self, code: str) -> List[str]:
        return self.token_pattern.findall(code)

    def _normalize_identifiers(self, tokens: List[str]) -> List[str]:
        # Normalize identifiers
        normalized_tokens = []
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.isidentifier():
                if token in self.keyword_dict:
                    normalized_tokens.append(self.keyword_dict[token])
                elif token in self.built_in_functions:
                    normalized_tokens.append(token)
                elif token.startswith('_'):
                    normalized_tokens.append('PRIVATE_IDENTIFIER')
                elif token in ['i', 'j', 'k', 'l', 'm', 'n']:
                    normalized_tokens.append('LOOP_VARIABLE')
                elif token[0].isupper() and not token.isupper():
                    normalized_tokens.append('CLASS_NAME')
                elif i > 0 and tokens[i - 1] == 'fun':
                    normalized_tokens.append('FUNCTION_NAME')
                elif i > 0 and tokens[i - 1] == 'class':
                    normalized_tokens.append('CLASS_NAME')
                elif token == "STRING_LITERAL":
                    normalized_tokens.append('STRING_LITERAL')
                elif token == "LITERAL":
                    normalized_tokens.append('LITERAL')
                else:
                    normalized_tokens.append('VARIABLE_NAME')
            elif token == '(':
                if i > 1 and normalized_tokens[-1] in {'FUNCTION_NAME', 'VARIABLE_NAME', 'CLASS_NAME',
                                                       'MEMBER_IDENTIFIER', 'PRIVATE_IDENTIFIER',
                                                       'LOOP_VARIABLE'} and normalized_tokens[-2] != 'fun' and \
                        normalized_tokens[-2] != 'class':
                    if normalized_tokens[-1] == 'CLASS_NAME':
                        normalized_tokens[-1] = 'CLASS_CONSTRUCTOR_CALL'
                    else:
                        normalized_tokens[-1] = 'FUNCTION_CALL'

                normalized_tokens.append(token)
            elif token == '@':
                if i < len(tokens) - 1 and tokens[i + 1].isidentifier():
                    normalized_tokens.append('@')
                    normalized_tokens.append('ANNOTATION')
                else:
                    normalized_tokens.append(token)
            else:
                normalized_tokens.append(token)

            i += 1

        return normalized_tokens
