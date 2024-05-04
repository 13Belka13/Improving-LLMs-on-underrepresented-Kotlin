import re

TOKEN_PATTERN = re.compile(r'\b\w+\b|[^\w\s]')
COMMENT_PATTERN = re.compile(r'#.*')
IMPORT_PATTERN = re.compile(r'^\s*(?:from\s+[\w.]+\s+)?import\s+(?:[^#\n]+|\(.*?\))', re.MULTILINE)
STRING_LITERAL_PATTERN = re.compile(r'(?:"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', re.MULTILINE)
NUMBER_LITERAL_PATTERN = re.compile(r'\b(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?\b')
ANNOTATION_PATTERN = re.compile(r'@\w+')