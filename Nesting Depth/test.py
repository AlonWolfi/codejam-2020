import os
from unittest import TestCase
from pathlib import Path

import filecmp


class Test(TestCase):
    def test(self):
        import filecmp
        from pathlib import Path

        input_file_name = Path('data') / 'input.in'
        test_file_name = Path('data') / 'test.out'
        py_file_name = 'main.py'
        output_file_name = 'pred.out'

        from main import main

        def input_gen():
            with open(input_file_name) as input_file:
                for line in input_file:
                    yield line.replace('\n', '')


        input_reader = input_gen()
        output_lines = []

        main(
            input_fnc=input_reader.__next__,
            print_fnc=output_lines.append
        )

        passed = True
        with open(test_file_name) as test_file:
            for i, (output_line, test_line) in enumerate(zip(output_lines, test_file)):
                output_line, test_line = output_line.replace('\n', ''), test_line.replace('\n', '')
                if output_line == test_line:
                    print(f'Case #{i} passed')
                else:
                    print(f'Case #{i} failed !!!!!')
                    print(output_line)
                    print(test_line)
                    passed = False
        self.assertTrue(passed)