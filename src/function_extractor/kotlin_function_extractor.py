import re


class KotlinFunctionExtractor:
    def __init__(self):
        self.function_pattern = re.compile(r'fun\s+(\w+)\s*\(([^)]*)\)\s*(\{.*?})', re.DOTALL)
        self.docstring_pattern = re.compile(r'/\*\*(.+?)\*/', re.DOTALL)
        self.string_literal_pattern = re.compile(r'"(?:\\.|[^"\\])*"')

    def extract_functions(self, code):
        functions = []

        code = self.string_literal_pattern.sub('""', code)

        for match in self.function_pattern.finditer(code):
            function_name = match.group(1)
            parameters = match.group(2)
            body = match.group(3)
            docstring_match = self.docstring_pattern.search(code, 0, match.start())
            docstring = docstring_match.group(1).strip() if docstring_match else ""

            function_data = {
                "signature": f"fun {function_name}({parameters})",
                "body": body,
                "docstring": docstring,
                "id": f"{len(functions)}"
            }
            functions.append(function_data)

            # Рекурсивный поиск вложенных функций
            nested_functions = self.extract_functions(body)
            functions.extend(nested_functions)

        return functions
