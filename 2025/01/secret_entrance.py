import sys
from typing import Generator

def get_turn_info(file_name: str) -> Generator[tuple[str, int]]:
    with open(file_name, "r") as f:
        for line in f:
            lr, *num_string = list(line.strip('\n'))
            num: int = int(''.join(num_string))
            yield (lr, num)

def num_revolutions(turn: tuple[str, int] | None) -> int:
    if turn is None: return 0
    turn_increment = turn[1]

    if turn_increment >= 100: return turn_increment // 100
    return 0

def passes_over_zero(position: int, turn: tuple[str, int]) -> int:
    passes_zero: int = num_revolutions(turn)
    turn_dir, turn_increment = turn
    if turn_dir not in ['L', 'R']: return -1

    # Don't want to include cases when the starting position IS zero - that would be double counting.
    if position > 0:
        if turn_dir == 'R' and position + turn_increment % 100 >= 100: passes_zero += 1
        if turn_dir == 'L' and position - turn_increment % 100 <= 0: passes_zero += 1
    
    return passes_zero

def turn_dial(position: int = 50, turn: tuple[str, int] | None = None) -> int:
    if turn is None: return position

    # Unpack the tuple into its elements
    turn_dir, turn_increment = turn
    if turn_dir not in ['L', 'R']: return -1
    return (position + turn_increment) % 100 if turn_dir == 'R' else (position - turn_increment) % 100



##### Main Program #####
def main() -> None:
    if len(sys.argv) < 2: raise RuntimeError('ERROR: Missing input file')
    
    position: int = 50
    stop_at_zero: int = 0
    passes_zero: int = 0

    for turn_info in get_turn_info(sys.argv[1]):
        # print(f"Number of times crosses zero: {turn_info} ===> {passes_over_zero(position, turn_info)}")
        passes_zero += passes_over_zero(position, turn_info)
        position = turn_dial(position, turn_info)
        # print(f"Turn: {turn_info}   ===>   {position}")
        # print(f'Number of full revolutions: {turn_info}  ===> {num_revolutions(turn_info)}')
        if position == 0: stop_at_zero += 1

    print(f'Number of times the dial stopped at zero position = {stop_at_zero}')
    print(f'Number of time the dial crossed zero = {passes_zero}')





if __name__ == '__main__':
    main()