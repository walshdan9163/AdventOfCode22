import os


def read_input(input_file_path):
    try:
        with open(input_file_path) as input:
            line = input.readline()
            while line:
                yield line
                line = input.readline()

    except Exception as e:
        print(f'Failed to read input: {e}')