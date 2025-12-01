import sys
from typing import List
from almanac import Almanac


def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    # almanac: List[str] = []
    almanac = Almanac()
    almanac_entry: str = ''

    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            # print(line, end=" ")
            if line:
                print(line, end=" ")
                almanac_entry = almanac_entry + line + ' '
            else:
                print()
                almanac_entry = almanac_entry.strip()
                # almanac.append(almanac_entry)
                almanac.input(almanac_entry)
                almanac_entry = ''
        
        print()
        almanac.input(almanac_entry)
        almanac.map_seeds()

    # almanac.show_seed_map()
    almanac.get_locations()

# Call main
if __name__ == "__main__":
    main()