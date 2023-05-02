import unittest

from segment import segment_source_code


class MyTestCase(unittest.TestCase):
    def test_something(self):
        file_path = 'llm.py'
        with open(file_path, 'r') as file:
            source_code = file.read()
        snippets = segment_source_code(source_code)

        # reconstitute the source code from the snippets and segment again
        new_snippets = segment_source_code("\n".join(snippets))
        self.assertEqual(snippets, new_snippets)


if __name__ == '__main__':
    unittest.main()
