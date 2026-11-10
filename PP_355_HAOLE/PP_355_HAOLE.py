# Contestant Number: HAO LE
from random import randrange as r


# Initial Message
WELCOME_PROMPT: str = "This application generates possible lock combinations; assuming that the numbers will be from 0 to 9 (inclusive). Please first enter the quantity of dials on the combination locks. And then enter how many combinations you would like to generate.\n\n\n"

# Dials
DIALS_PROMPT: str = "Each lock has how many dials? "
DIALS_ERROR_PROMPT: str = "Please enter an integer greater than or equal to 3.\n"

# Number of Combinations
COMBINATIONS_NUMBER_PROMPT: str = "How many combinations should I generate? "
COMBINATIONS_NUMBER_ERROR_PROMPT: str = "Please enter an integer greater than or equal to 1.\n"

COMBINATIONS_LIST: list[str] = []

SEPARATOR: str = "-" * 30

def get_number_of_dials() -> int:
    dials: int

    while True:
        try:
            dials = int(input(DIALS_PROMPT))
        except ValueError:
            print(DIALS_ERROR_PROMPT)
            continue

        if dials < 3:
            print(DIALS_ERROR_PROMPT)
        else:
            return dials

def get_how_many_to_list() -> int:
    combinations: int

    while True:
        try:
            combinations = int(input(COMBINATIONS_NUMBER_PROMPT))
        except ValueError:
            print(COMBINATIONS_NUMBER_ERROR_PROMPT)
            continue

        if combinations < 1:
            print(COMBINATIONS_NUMBER_ERROR_PROMPT)
        else:
            return combinations

def get_number(num1: int, num2: int) -> int:
    return r(num1, num2 + 1) if num1 <= num2 else r(num2, num1 + 1)

def next_combo_number(number_of_combinations: int) -> str:
    new_entry: str = " ".join([str(get_number(0, 9)) for _ in range(number_of_combinations)])

    while new_entry in COMBINATIONS_LIST:
        new_entry: str = " ".join([str(get_number(0, 9)) for _ in range(number_of_combinations)])

    COMBINATIONS_LIST.append(new_entry)
    return new_entry

print(WELCOME_PROMPT)

number_of_dials:int = get_number_of_dials()
print()

n_of_combinations: int = get_how_many_to_list()
print()

print(SEPARATOR)
print()

for i in range(n_of_combinations):
    print(f"Number {i + 1}: {next_combo_number(number_of_dials)}\n")

print(SEPARATOR)
print()

print(f"{n_of_combinations} random combinations were generated")