import os

from starting_crate_stacks import test_starting_crate_stacks, actual_starting_crate_stacks


curr_path = os.path.join(os.getcwd(), '5')

def get_step_details(step):
    split_step = step.split()
    num_to_move = int(split_step[1])
    move_from = split_step[3]
    move_to = split_step[5]
    return num_to_move, move_from, move_to


def solve(input_file, crate_stacks):
    input_file_path = os.path.join(curr_path, input_file)
    with open(input_file_path) as input:
        steps = input.read().splitlines()

    for step in steps:
        crates = []
        num_to_move, move_from, move_to = get_step_details(step)
        for count in range(num_to_move):
            crates.append(crate_stacks[move_from].pop())
        crates = reversed(crates)
        crate_stacks[move_to] += crates

    top_crates = ''
    for key in crate_stacks.keys():
        top_crates += crate_stacks[key][-1]
    
    return top_crates


def main():
    test_result = solve('test_input.txt', test_starting_crate_stacks)
    actual_result = solve('input.txt', actual_starting_crate_stacks)
    print(f'Test result = {test_result}')
    print(f'Actual result = {actual_result}')

if __name__ == '__main__':
    main()