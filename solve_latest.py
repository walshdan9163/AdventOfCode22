import os
import importlib


def solve_day(day: str):
    problem_one_solve = importlib.import_module(f'{day}.one')
    problem_two_solve = importlib.import_module(f'{day}.two')
    print('Problem One:')
    problem_one_solve.main()
    print('\nProblem Two:')
    problem_two_solve.main()


def get_latest_day() -> str:
    dir_contents = os.listdir(os.getcwd())
    folders = []
    for content in dir_contents:
        if not os.path.isfile(content):
            folders.append(content)
    folders = sorted(folders)
    latest_day = folders[-1]
    return latest_day


if __name__ == '__main__':
    importlib.invalidate_caches()
    day = get_latest_day()
    solve_day(day)
