import sys
from typing import Generator

def get_battery_bank(file_name: str) -> Generator[list[int]]:
    with open(file_name) as f:
        for line in f:
            line = line.strip('\n')
            yield [int(s) for s in line]

def get_maximum_joltage(battery_bank: list[int]) -> int:
    joltage_1: int = 0
    joltage_2: int = 0

    for current_joltage, next_joltage in zip(battery_bank, battery_bank[1:]):
        # print(f"Current: {current_joltage}, Next: {next_joltage}")
        if current_joltage > joltage_1:
            joltage_1 = current_joltage
            joltage_2 = next_joltage
            # print(f'J1 = {joltage_1}, J2 = {joltage_2}')
            continue

        if  next_joltage > joltage_2:
            joltage_2 = next_joltage
            # print(f'J2 = {joltage_2}')
    
    return int(f'{joltage_1}{joltage_2}')

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')
    
    max_joltage: list[int] = []
    for battery_bank in get_battery_bank(sys.argv[1]):
        print(f"{battery_bank} -> {get_maximum_joltage(battery_bank)}")
        max_joltage.append(get_maximum_joltage(battery_bank))

    print(f'List of maximum joltages: {max_joltage}')
    print(f'Total Joltage: {sum(max_joltage)}')


# Call main
if __name__ == "__main__":
    main()