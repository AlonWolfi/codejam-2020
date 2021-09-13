import os
from unittest import TestCase
from pathlib import Path
class Test(TestCase):
    def test(self):
        input_file_name = Path('data') / 'input.in'
        test_file_name = Path('data') / 'test.out'
        py_file_name = 'main.py'
        output_file_name = 'pred.out'
        os.popen(f"python {py_file_name} < {input_file_name} > {output_file_name}")
        output_file = open(output_file_name)
        test_file = open(test_file_name)

        for output_line, test_line in zip(output_file, test_file):
            print(output_line)
            print(test_line)
            self.assertEqual(output_line, test_line)
