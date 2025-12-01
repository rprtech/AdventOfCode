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
        scratchcard = dict(id = int(id), winning_numbers = winning_numbers, game_numbers = game_numbers, copies = 0)
        
        scratchcards.append(scratchcard)

    return scratchcards

def check_win(winning_numbers: List[int], game_numbers: List[int]) -> List[int]:
    return list(set(winning_numbers).intersection(game_numbers))

def get_score(number: int) -> int:
    return 2 ** (number - 1)

def update_copies(idx: int, num_matches: int, scratchcards: List[dict]) -> None:
    start_idx = idx + 1
    end_idx = start_idx + num_matches
    
    for card_idx in range(start_idx, end_idx):
        scratchcards[card_idx]['copies'] += 1


def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    with open(sys.argv[1]) as f:
        scratchcards = get_scratchcards(f)
    
    scores = []
    total_cards = [len(scratchcards)]
    card_index: int = 0

    for scratchcard in scratchcards:
        # print(f'Card ID = {scratchcard["id"]}')
        matching_numbers = check_win(scratchcard['winning_numbers'], scratchcard['game_numbers'])
        print(f'{matching_numbers} => Copies: {scratchcard["copies"]}')
        # scores.append(get_score(len(matching_numbers)) if len(matching_numbers) > 0 else 0)

        if len(matching_numbers) > 0:
            scores.append(get_score(len(matching_numbers)))

            # Update the copies of subsequent cards based on this (original card) plus its copies
            for _ in range(scratchcard['copies'] + 1):
                update_copies(card_index, len(matching_numbers), scratchcards)

        total_cards.append(scratchcard['copies'])
        card_index += 1

    print(f'Scores: {scores}')
    print(f'Sum of scores: {sum(scores)}')
    print(f'Cards and copies: {total_cards}')
    print(f'Total Scratchcards: {sum(total_cards)}')


# Call main
if __name__ == "__main__":
    main()