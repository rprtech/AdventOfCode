import sys
from typing import Tuple


def validate_play_sets(play_sets: str) -> bool:
    def is_play_valid(_play: str) -> bool:
        rgb_constraint = {
            'red': 12,
            'green': 13,
            'blue': 14
        }

        # print(f'Play: {_play}')

        # Check each color against rgb_constraint
        for numColor in _play.split(','):
            number, color = numColor.split()
            # print(f'{color} => {number}\tContraint = {rgb_constraint[color]}')

            # Stop processing and return false as soon as a constraint violation is detected.
            if int(number) > rgb_constraint[color]: return False

        return True
    
    plays = play_sets.split(';')
    # print(f'Plays: {plays}')

    for play in plays:
        # If a play is not valid, return False; don't bother checking the other plays
        if not is_play_valid(play): return False

    return True

def minimum_cube_set(play_sets: str) -> Tuple[int, int, int]: 
    rgb_minimum = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    def update_min_rgb(_play: str) -> None:
        for numColor in _play.split(','):
            number, color = numColor.split()

            if int(number) > rgb_minimum[color]: rgb_minimum[color] = int(number)

    plays = play_sets.split(';')
    # print(f'Plays: {plays}')
    for play in plays: update_min_rgb(play)
    return (rgb_minimum['red'], rgb_minimum['green'], rgb_minimum['blue'])

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    valid_games = []
    cube_power = []

    with open(sys.argv[1]) as f:
        for line in f:
            game, play_sets = (line.strip()).split(':')
            _, game_id = game.split()
            # print(f'\nGame ID: {game_id}\t Play Set: {play_sets}')

            if validate_play_sets(play_sets): valid_games.append(int(game_id))
            r,g,b = minimum_cube_set(play_sets)
            cube_power.append(r*g*b)

    print(f'\n\nValid Games: {valid_games}')
    print(f'Sum of valid games: {sum(valid_games)}')
    print(f'\n\nCube Power: {cube_power}')
    print(f'Sum of powers: {sum(cube_power)}\n')



### Call Main ###
if __name__ == '__main__':
    main()