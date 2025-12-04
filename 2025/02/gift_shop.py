import sys
from typing import Generator

def check_id_validity(id: str) -> bool:
    # print(f"Checking ID: {id}")
    id_char_list: list[str] = list(id)
    split_idx: int = len(id_char_list) // 2
    first_half: list[str] = id_char_list[:split_idx]
    second_half: list[str] = id_char_list[split_idx:]

    if first_half == second_half:
        # print(f"\tChecking ID: {id} -> [{''.join(first_half)}] = [{''.join(second_half)}]")
        return True
    
    return False

def check_repeating_sequence(id: str) -> bool:
    split_idx: int = (len(id) // 2) + (len(id) % 2)
    # print(f"Checking for repeating sequence: {id} -> split idx = {split_idx}")

    chunk_list: list[str] = []
    repeating_sequence: bool = False

    for chunk in range(split_idx, 0, -1):
        chunk_list = [id[i:i+chunk] for i in range(0, len(id), chunk)]
        reference_string: str = chunk_list.pop(0)
        repeating_sequence = True

        for check_string in chunk_list:
            if not repeating_sequence: continue
            if reference_string == check_string:
                repeating_sequence = True
                continue
            else:
                repeating_sequence = False

        if repeating_sequence:
            print(f"\t{id}   --->   {chunk_list}   ---> {reference_string}")
            return True
            
    return False
    

def get_range(file_name) -> Generator[tuple[int, int]]:
    id_ranges: list[str] = []

    with open(file_name) as f:
        for line in f:
            line = line.strip('\n')
            id_ranges = line.split(',')
    
    for id_range in id_ranges:
        rng_low, rng_high = id_range.split('-')
        yield (int(rng_low), int(rng_high))
        

def is_num_chars_even(char_string: str) -> bool:
    if len(list(char_string)) % 2 == 0: return True
    return False

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')
    
    invalid_ids: list[int] = []
    repeated_seq_ids: list[int] = []
    
    for prod_range in get_range(sys.argv[1]):
        print(f"Range: {prod_range}")
        for prod_id in range(prod_range[0], prod_range[1] + 1):
            prod_id_str = str(prod_id)
            
            if check_repeating_sequence(prod_id_str): repeated_seq_ids.append(prod_id)
            if not is_num_chars_even(prod_id_str): continue
            if check_id_validity(prod_id_str): invalid_ids.append(prod_id)

    print(f"Sum of invalid ids is: {sum(invalid_ids)}")
    print(f"Sum of IDs with repeated sequence is: \n\t- All sum {sum(repeated_seq_ids)}  \n\t- Set sum {sum(set(repeated_seq_ids))}")
    # print(f'Repeated Sequence List: {repeated_seq_ids}')


# Call main
if __name__ == "__main__":
    main()