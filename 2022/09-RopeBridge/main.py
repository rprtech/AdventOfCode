import sys
from rope import Rope, Knot

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    r_part1 = Rope()
    r_part2 = Rope(num_knots=10)
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip('\n')
            dir, dist = line.split()
            print(f'MOVE: {line}')
            #r_part1.move(direction=dir, distance=dist, show = True)
            r_part2.move(direction=dir, distance=dist, show=True)

    print(f'Number of positions visited by tail is = {len(set(r_part2.knots[-1].history))}')



### Call Main ###
if __name__ == "__main__":
    main()