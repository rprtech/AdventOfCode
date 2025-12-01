import sys
from typing import List

def get_partnumbers(grid: list) -> List[int]:
    MAX_ROWS = len(grid)
    
    # Since I am treating the data as being in a grid; I am assuming that each row are of equal length
    # If they are not, this code will break.
    # However, sticking with my assumption, I will get the MAX_COLS by just looking at the first row
    MAX_COLS = len(grid[0])

    def range_inclusive(start: int, end: int) -> range:
        '''Defined for code readability'''
        return range(start, end + 1)

    def check_adjacent(row: int, col: int) -> bool:
        # print(f'Check for symbols adjacent to "{grid[x][y]}" at location [{x},{y}]')
        
        for x in range_inclusive(row - 1, row + 1):
            if x < 0 or x >= MAX_ROWS: continue
            # print(f'Valid X = {x}')

            for y in range_inclusive(col - 1, col + 1):
                if y < 0 or y >= MAX_COLS: continue
                if x == row and y == col: continue
                # print(f'Valid Y = {y}')
                adjacent_char = str(grid[x][y])
                if not (adjacent_char.isdigit() or adjacent_char == '.'): return True
                
        return False

    part_numbers = []

    for row in range(MAX_ROWS):
        # This temporary number list will hold digit characters to reconstruct the number
        tmp_num = []
        adjacent_symbol = False

        for col in range(MAX_COLS):
            current_char = grid[row][col]
            # print(f'{current_char}', end = " ")

            if str(current_char).isdigit():
                tmp_num.append(current_char)
                if not adjacent_symbol: adjacent_symbol = check_adjacent(row, col)
            else:
                if len(tmp_num) > 0 and adjacent_symbol: part_numbers.append(int("".join(tmp_num)))
                # if len(tmp_num) > 0:
                #     if adjacent_symbol:
                #         part_numbers.append(int("".join(tmp_num)))
                #     else:
                #         print(f'\tPosition: [{row},{col}]\t --> {int("".join(tmp_num))}')
                adjacent_symbol = False
                tmp_num = []
        
        # Handle the case when the number is at the right edge (no more characters to trigger the above else block)
        if len(tmp_num) > 0 and adjacent_symbol: part_numbers.append(int("".join(tmp_num)))

        # print()
    return part_numbers

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')
    
    grid = []

    with open(sys.argv[1]) as f:
        # Add each row as a tuple
        for line in f: grid.append(tuple([*line.strip()]))
    
    # Convert the grid from a list to a tuple.
    # Also note, that by calling this a "grid" it assumes that each row has the same length
    grid = tuple(grid)
    # print(grid)

    part_numbers = get_partnumbers(grid)
    print(f'\n\nPartNumbers: {part_numbers}')
    print(f'\nThe sum of all part numbers is: {sum(part_numbers)}\n')

### Call Main ###
if __name__ == '__main__':
    main()