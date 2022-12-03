import os


curr_path = os.path.join(os.getcwd(), '1')


def solve(input_file):
    input_file_path = os.path.join(curr_path, input_file)

    with open(input_file_path) as input:
        cals_list = input.readlines()

    max_cals = 0
    curr_cals = 0
    for cals in cals_list:
        if cals != '\n':
            curr_cals += int(cals)
            max_cals = max(max_cals, curr_cals)
        else:
            curr_cals = 0

    return max_cals

def main():
    test_result = solve('test_input.txt')
    actual_result = solve('input.txt')
    print(f'Test result = {test_result}')
    print(f'Actual result = {actual_result}')

if __name__ == '__main__':
    main()