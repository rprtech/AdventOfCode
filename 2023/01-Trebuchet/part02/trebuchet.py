import sys
from typing import List

def get_firstLastDigitStr(line: str) -> List[str]:
    
    def _get_digit(internalListt: list, digitWords: tuple) -> str:
        letters = []

        for char in internalListt:
        
            if str(char).isdigit():
                return str(char)
            
            # At this point the character is not a digit.  Add it to the letters list
            # then check if any of the "spelledDigits" are contained in the collection of letters
            # If the digit is spelled out, return the text representation of the digit
            letters.append(str(char))

            for word in digitWords:
                if word in "".join(letters): return str(digitWords.index(word))
            
        return '-1'

    spelledDigits = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

    def _first_digit(internalList: list) -> None:
        digits.append(_get_digit(internalList, spelledDigits))
        

    def _last_digit(internalList: list) -> None:
        # Reverse the spelling of each digit when processing the list in reverse order
        tmpReverse = []

        for word in spelledDigits:
            word_letters = [*word]
            word_letters.reverse()
            tmpReverse.append("".join(word_letters))

        spelledDigitsReverse = tuple(tmpReverse)
        internalList.reverse()
        digits.append(_get_digit(internalList, spelledDigitsReverse))


    digits = []

    _first_digit([*line])
    _last_digit([*line])

    return digits

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    calibration_values = []

    with open(sys.argv[1]) as f:
        for line in f:
            digits_str_list = get_firstLastDigitStr(line.strip())
            calibration_values.append(int("".join(digits_str_list)))
            # print(f'Calibration Values: {calibration_values}')

    print(f'Sum of Calibration Values: {sum(calibration_values)}')

### Call Main ###
if __name__ == '__main__':
    main()