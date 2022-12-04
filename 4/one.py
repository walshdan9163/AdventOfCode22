import os

from ..helpers import read_input


def solve(input_file):
    input_file_path = os.path.join(os.getcwd(), '4', input_file)
    for line in read_input(input_file_path):
        print(line)

def main():
    test_result = solve('test_input.txt')
    actual_result = solve('input.txt')
    print(f'Test result = {test_result}')
    print(f'Actual result = {actual_result}')

if __name__ == '__main__':
    main()