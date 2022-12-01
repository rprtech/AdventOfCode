import sys

def count_calories(file_name) -> list[int]:
    calorie_list = []

    with open(file_name) as f:
        idx = 0
        calorie_list.append(0)

        for line in f:
            if line.strip():
                calorie_list[idx] += int(line.strip())
            else:
                idx += 1
                calorie_list.append(0)

    return calorie_list

### Main ###

if len(sys.argv) < 2:
    raise RuntimeError(
        'ERROR:  Datafile is missing'
    )

calorie_list = count_calories(sys.argv[1])
calorie_list.sort(reverse=True)

if len(sys.argv) == 3:
    n = int(sys.argv[2].strip())
else:
    n = 1

print(f'The top {n} most calories are: {calorie_list[0:n]}')
print(f'The total calories of the top {n} is: {sum(calorie_list[0:n])}')
