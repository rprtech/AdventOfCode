import sys
from typing import List

class CleanupAssignment:
    total_full_containment: int = 0
    total_overlap: int = 0

    @classmethod
    def __increment_full_containment(cls) -> None:
        cls.total_full_containment += 1

    @classmethod
    def __increment_overlap(cls) -> None:
        cls.total_overlap += 1

    def _assign_cleanup(self, rng_list: List[str]) -> List:
        assigned_elf = []

        for rng in rng_list:
            start, stop = rng.split('-')
            assigned_elf.append(dict(start = int(start), stop = int(stop)))

        return assigned_elf


    def _is_fully_contained(self) -> bool:
        """
        This method could be written better by converting to sets then using the 'issubset' method.
        See _is_overlapping method below for creating sets.  Maybe these 2 functions could be combined.
        REMEMBER: If fully_contained is True, then overlap is also True
        """
        elf1 = 0
        elf2 = 1

        if self.elf[elf1]['start'] <= self.elf[elf2]['start'] and self.elf[elf1]['stop'] >= self.elf[elf2]['stop']:
            return True
        
        if self.elf[elf2]['start'] <= self.elf[elf1]['start'] and self.elf[elf2]['stop'] >= self.elf[elf1]['stop']:
            return True
        
        return False

    def _is_overlapping(self) -> bool:
        elf1_sections = set(range(self.elf[0]['start'], self.elf[0]['stop'] + 1))
        elf2_sections = set(range(self.elf[1]['start'], self.elf[1]['stop'] + 1))

        return True if len(elf1_sections.intersection(elf2_sections)) > 0 else False

    def __init__(self, rng_list: List[str]) -> None:
        #print(f'Received ranges: {rng_list}')
        self.elf = self._assign_cleanup(rng_list)
        self.full_containment: bool = self._is_fully_contained()
        self.overlap: bool = self._is_overlapping()

        if self.full_containment:
            CleanupAssignment.__increment_full_containment()

        if self.overlap:
            CleanupAssignment.__increment_overlap()


def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    assignments = []

    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip('\n')
            assignments.append(CleanupAssignment(line.split(',')))

    print(f'Full Containment = {CleanupAssignment.total_full_containment}')
    print(f'Overlap = {CleanupAssignment.total_overlap}')


### Call main ###
if __name__ == '__main__':
    main()