from typing import Dict
import sys


# GLOBAL - to prevent multiple re-evaluation of the same data
paper_grid: list[list[str]] = []
dimension: Dict[str, int] = {
    "rows": 0,
    "columns": 0
}

def count_neighbors(current_postition: tuple[int, int]) -> int:
    this_row, this_col = current_postition
    check_sequence: list[int] = [-1, 0, 1]
    neighbors: int = 0

    for row in check_sequence:
        if this_row + row not in range(dimension['rows']): continue

        for col in check_sequence:
            if this_col + col not in range(dimension['columns']): continue
            # Don't include the current position in the count
            if row == 0 and col == 0: continue
            if paper_grid[this_row + row][this_col + col] == '@': neighbors += 1

    return neighbors

def print_grid() -> None:
    for row in paper_grid:
        print(row)

def remove_rolls(max_neighbors: int = 3) -> tuple[int, list[tuple[int, int]]]:
    accessible_rolls: int = 0
    positions_removed: list[tuple[int, int]] = []

    for row, sub_list in enumerate(paper_grid):
        for col, item in enumerate(sub_list):
            if item == '.': continue
            if count_neighbors((row, col)) <= 3:
                accessible_rolls += 1
                positions_removed.append((row, col))
                # print(f'{accessible_rolls}: ({row}, {col}) - {item} -> Neighbors = {count_neighbors((row, col))}')

    return (accessible_rolls, positions_removed)

def update_grid(positions_removed: list[tuple[int, int]]) -> None:
    for position in positions_removed:
        r, c = position
        paper_grid[r][c] = '.'

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip('\n')
            paper_grid.append(list(line))
            
    dimension['rows'] = len(paper_grid)
    # For columns, I am assuming that all rows have the same number of characters (columns)
    # so, for simplicity, I am getting the number of colums from just the list in the top row.
    dimension['columns'] = len(paper_grid[0])

    # print_grid()
    total_rolls_removed, positions_removed = remove_rolls()
    print(f"Number of rolls removed = {total_rolls_removed}")

    while (len(positions_removed) > 0):
        update_grid(positions_removed)
        # print_grid()
        rolls_removed, positions_removed = remove_rolls()
        total_rolls_removed += rolls_removed

    print(f"Iterative removal resulted in {total_rolls_removed} being removed")


# Call main
if __name__ == "__main__":
    main()