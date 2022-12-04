import sys
from typing import List

class CleanupAssignment:
    total_full_containment: int = 0

    @classmethod
    def __increment_full_containment(cls) -> None:
        cls.total_full_containment += 1

    def _assign_cleanup(self, rng_list: List[str]) -> List:
        assigned_elf = []

        for rng in rng_list:
            start, stop = rng.split('-')
            assigned_elf.append(dict(start = int(start), stop = int(stop)))

        return assigned_elf


    def _is_fully_contained(self) -> bool:
        elf1 = 0
        elf2 = 1

        if self.elf[elf1]['start'] <= self.elf[elf2]['start'] and self.elf[elf1]['stop'] >= self.elf[elf2]['stop']:
            return True
        
        if self.elf[elf2]['start'] <= self.elf[elf1]['start'] and self.elf[elf2]['stop'] >= self.elf[elf1]['stop']:
            return True
        
        return False



    def __init__(self, rng_list: List[str]) -> None:
        #print(f'Received ranges: {rng_list}')
        self.elf = self._assign_cleanup(rng_list)
        self.full_containment: bool = self._is_fully_contained()

        if self.full_containment:
            CleanupAssignment.__increment_full_containment()


def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    assignments = []

    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip('\n')
            assignments.append(CleanupAssignment(line.split(',')))

    print(f'Full Containment = {CleanupAssignment.total_full_containment}')


### Call main ###
if __name__ == '__main__':
    main()