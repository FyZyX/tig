import ast


class SnippetVisitor(ast.NodeVisitor):
    def __init__(self, source_lines):
        self.source_lines = source_lines
        self.snippets = []
        self.current_end_line = 0

    def add_snippet(self, start_line, end_line):
        snippet = self.source_lines[start_line:end_line]
        snippet_text = '\n'.join(snippet)
        if snippet_text.strip():
            self.snippets.append(snippet_text.strip("\n"))
        else:
            self.snippets[-1] += snippet_text.strip("\n")
        self.current_end_line = end_line

    def visit_FunctionDef(self, node):
        start_line = self.current_end_line
        end_line = node.lineno - 1
        self.add_snippet(start_line, end_line)
        self.add_snippet(node.lineno - 1, node.end_lineno)
        self.current_end_line = node.end_lineno
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.visit_AsyncFunctionDef(node)

    def visit_ClassDef(self, node):
        start_line = self.current_end_line
        end_line = node.lineno - 1
        self.add_snippet(start_line, end_line)
        self.current_end_line = node.lineno - 1
        self.generic_visit(node)
        self.add_snippet(self.current_end_line, node.end_lineno)


def segment_source_code(source_code):
    source_lines = source_code.splitlines()
    tree = ast.parse(source_code)

    snippet_visitor = SnippetVisitor(source_lines)
    snippet_visitor.visit(tree)

    # Add remaining code after the last visited node
    snippet_visitor.add_snippet(snippet_visitor.current_end_line, len(source_lines))

    return snippet_visitor.snippets


def main():
    file_path = "llm.py"
    with open(file_path, "r") as file:
        source_code = file.read()
    snippets = segment_source_code(source_code)

    for i, snippet in enumerate(snippets):
        print(f"Snippet {i + 1}:")
        print("-" * 40)
        print(snippet)
        print()


if __name__ == '__main__':
    main()
