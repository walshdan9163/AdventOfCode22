import os

from .helpers import their_options, my_options, their_win_outcomes, my_win_outcomes, ties_map, points_map


curr_path = os.path.join(os.getcwd(), '2')


def calculate_score(outcome: str) -> int:
    their_choice = outcome[0]
    need_outcome = outcome[-1]
    outcome_score = 0
    if need_outcome == 'X':
        my_choice = their_win_outcomes[their_choice]
    elif need_outcome == 'Y':
        outcome_score = 3
        my_choice = ties_map[their_choice]
    elif need_outcome == 'Z':
        outcome_score = 6
        my_choice = my_win_outcomes[their_choice]
    
    my_choice_score = points_map[my_choice]
    return outcome_score + my_choice_score


def solve(input):
    input_path = os.path.join(curr_path, input)

    possible_outcomes = [their_choice + ' ' + my_choice for their_choice in their_options for my_choice in my_options]

    score_map = {}
    for outcome in possible_outcomes:
        score_map[outcome] = calculate_score(outcome)

    with open(input_path) as input:
        round_outcomes = input.read().splitlines()

    total_score = 0
    for round in round_outcomes:
        total_score += score_map[round]

    return str(total_score)


def main():
    test_result = solve('test_input.txt')
    actual_result = solve('input.txt')
    print(f'Test result = {test_result}')
    print(f'Actual result = {actual_result}')


if __name__ == '__main__':
    main()
    