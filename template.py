import sys


def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    with open(sys.argv[1]) as f:
        for line in f:
            pass


# Call main
if __name__ == "__main__":
    main()