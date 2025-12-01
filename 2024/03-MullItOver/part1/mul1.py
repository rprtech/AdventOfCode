import re
import sys

def mul(m: int, n: int) -> int:
    return m*n

def main() -> None:
    # print(f'Arguments are: {sys.argv}')
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')
    
    line_sum: list[int] = []

    with open(sys.argv[1]) as f:
        for line in f:
            # print(f'LINE: {line}')
            regex: str =r'mul\(\d+,\d+\)'
            valid_mul: list = re.findall(regex, line)
            # print(f'RESULT: {valid_mul}')

            for mul_op in valid_mul:
                # print(f'PRODUCT = {eval(mul_op)}')
                line_sum.append(eval(mul_op))

    print(line_sum)
    print(sum(line_sum))
    pass

# Call main
if __name__ == "__main__":
    main()