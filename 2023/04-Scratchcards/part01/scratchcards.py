import sys
from io import TextIOWrapper
from typing import List

def get_scratchcards(file_handle: TextIOWrapper) -> List[dict]:
    scratchcards = []

    for line in file_handle:
        line = line.strip()
        card, all_numbers = line.split(':')
        _, id = card.split()
        winning_numbers, game_numbers = all_numbers.split('|')

        # Use list comprehension to cast the string of winning_numbers and game_numbers to integers
        winning_numbers = [int(wn) for wn in winning_numbers.split()]
        game_numbers = [int(gn) for gn in game_numbers.split()]
        scratchcard = dict(id = int(id), winning_numbers = winning_numbers, game_numbers = game_numbers)
        
        scratchcards.append(scratchcard)

    return scratchcards

def check_win(winning_numbers: List[int], game_numbers: List[int]) -> List[int]:
    return list(set(winning_numbers).intersection(game_numbers))

def get_score(number: int) -> int:
    return 2 ** (number - 1)

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    with open(sys.argv[1]) as f:
        scratchcards = get_scratchcards(f)
    
    scores = []

    for scratchcard in scratchcards:
        print(check_win(scratchcard['winning_numbers'], scratchcard['game_numbers']))
        matching_numbers = check_win(scratchcard['winning_numbers'], scratchcard['game_numbers'])
        scores.append(get_score(len(matching_numbers)) if len(matching_numbers) > 0 else 0)

    print(f'Scores: {scores}')
    print(f'Sum of scores: {sum(scores)}')


# Call main
if __name__ == "__main__":
    main()