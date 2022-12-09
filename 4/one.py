import os


curr_path = os.path.join(os.getcwd(), '4')

def solve(input_file):
    input_file_path = os.path.join(curr_path, input_file)

    with open(input_file_path) as input:
        id_pairs = input.read().splitlines()

    overlap_count = 0

    for pair in id_pairs:
        elf_one_ids, elf_two_ids = pair.split(',')
        elf_one_ids = elf_one_ids.split('-')
        elf_two_ids = elf_two_ids.split('-')

        if (elf_one_ids[0] <= elf_two_ids[0] and elf_one_ids[1] >= elf_two_ids[1]) or (elf_two_ids[0] <= elf_one_ids[0] and elf_two_ids[1] >= elf_one_ids[1]):
            overlap_count += 1

    return overlap_count


def main():
    test_result = solve('test_input.txt')
    actual_result = solve('input.txt')
    print(f'Test result = {test_result}')
    print(f'Actual result = {actual_result}')

if __name__ == '__main__':
    main()