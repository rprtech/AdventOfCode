import sys
from typing import List

def get_firstLastDigitStr(char_list:list) -> List[str]:
    
    def _get_digit(_internalListt: list) -> str:
        for char in _internalListt:
        
            if str(char).isdigit():
                return str(char)
            
        return '-1'
    
    digits = []
    digits.append(_get_digit(char_list))
    
    char_list.reverse()
    
    digits.append(_get_digit(char_list))

    return digits

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    calibration_values = []

    with open(sys.argv[1]) as f:
        for line in f:
            digits_str_list = get_firstLastDigitStr([*line])
            calibration_values.append(int("".join(digits_str_list)))
            # print(f'Calibration Values: {calibration_values}')

    print(f'Sum of Calibration Values: {sum(calibration_values)}')

### Call Main ###
if __name__ == '__main__':
    main()