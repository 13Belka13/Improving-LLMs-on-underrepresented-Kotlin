import re

TOKEN_PATTERN = re.compile(r'\b\w+\b|[^\w\s]')
COMMENT_PATTERN = re.compile(r'/\*[\s\S]*?\*/|//.*')
IMPORT_PATTERN = re.compile(r'^\s*import\s.*', re.MULTILINE)
PACKAGE_PATTERN = re.compile(r'^\s*package\s.*', re.MULTILINE)
STRING_LITERAL_PATTERN = re.compile(r'"[^"]*"', re.MULTILINE)
NUMBER_LITERAL_PATTERN = re.compile(r'\b\d+(\.\d+)?\b', re.MULTILINE)
ANNOTATION_PATTERN = re.compile(r'@\w+')