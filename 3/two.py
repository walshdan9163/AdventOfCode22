import os
import string

curr_folder = os.path.join(os.getcwd(), '3')

char_to_int_map = {}
lower_char_to_int_map = dict(zip(string.ascii_lowercase, [ord(char) - 96 for char in string.ascii_lowercase]))
upper_char_to_int_map = dict(zip(string.ascii_uppercase, [ord(char) - 38 for char in string.ascii_uppercase]))
char_to_int_map.update(lower_char_to_int_map)
char_to_int_map.update(upper_char_to_int_map)


def solve(input_file):
    input_path = os.path.join(curr_folder, input_file)

    with open(input_path) as input:
        rucksack_contents = input.read().splitlines()

    total_priority = 0
    sack_one_contents = None
    sack_two_contents = None
    sack_three_contents = None

    for index, contents in enumerate(rucksack_contents):
        if index % 3 == 0:
            sack_one_contents = contents
        elif index % 3 == 1:
            sack_two_contents = contents
        elif index % 3 == 2:
            sack_three_contents = contents
            common_char = list(set(sack_one_contents)&set(sack_two_contents)&set(sack_three_contents))[0]
            total_priority += char_to_int_map[common_char]

    return total_priority

def main():
    test_result = solve('test_input.txt')
    actual_result = solve('input.txt')
    print(f'Test result = {test_result}')
    print(f'Actual result = {actual_result}')


if __name__ == '__main__':
    main()
    