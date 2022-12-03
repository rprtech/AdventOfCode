import sys
import string
from typing import Tuple

#def build_priorities_list() -> dict:
#    priorities = {}
#
#   for priority, letter in enumerate(string.ascii_lowercase, start=1):
#        priorities[letter] = priority
#
#    for priority, letter in enumerate(string.ascii_uppercase, start=27):
#        priorities[letter] = priority
#    
#    return priorities

class Rucksack:
    priorities = {}
    total_priorities: int = 0

    @classmethod
    def build_priorities_list(cls) -> None:
        for priority, letter in enumerate(string.ascii_lowercase, start=1):
            cls.priorities[letter] = priority

        for priority, letter in enumerate(string.ascii_uppercase, start=27):
            cls.priorities[letter] = priority


    @classmethod
    def __set_total_priorities(cls, priority: int) -> None:
        cls.total_priorities += priority


    def _identify_common_items(self) -> None:
        self.common_items: str = []

        for ltr in self.compartment1:
            if ltr in self.compartment2 and ltr not in self.common_items:
                self.common_items.append(ltr)

    def _set_priority(self) -> None:
        for item in self.common_items:
            self.priority += self.priorities[item]


    def __init__(self, items: str) -> None:
        total_items = len(items)
        self.all_items = items
        self.compartment1 = items[0:int(total_items/2)]
        self.compartment2 = items[int(total_items/2):]
        self.priority: int = 0

        self._identify_common_items()
        self._set_priority()
        Rucksack.__set_total_priorities(self.priority)


class ElfGroup:
    __all_groups = []
    total_priority: int = 0

    @classmethod
    def make_groups(cls, rucksacks: list[Rucksack], max_members: int = 3):
        #print(f'Total rucksacks are: {len(rucksacks)}')

        """
        This is to prevent an out of bounds error.  If len(rucksacks) is a multiple
        of max_members, then each group will comprise of max_members rucksacks.  If
        however, it is not a multiple, then the last group will have fewer than 
        max_members.  To prevent the out of bounds error, the final group will be
        created like so: rucksacks[int(last_slice_idx):]
        """
        last_slice_idx: int = len(rucksacks) - (len(rucksacks) % max_members)

        for slice_start_idx in range(0, len(rucksacks), max_members):
            if slice_start_idx == last_slice_idx:
                #print(f'{slice_start_idx} (LAST) - Appending {len(rucksacks[int(slice_start_idx)::])} rucksacks')
                cls.__all_groups.append(cls(rucksacks[int(slice_start_idx)::], slice_start_idx))
            else:
                #print(f'{slice_start_idx} - Appending {len(rucksacks[int(slice_start_idx):int(slice_start_idx + max_members)])} rucksacks')
                cls.__all_groups.append(cls(rucksacks[int(slice_start_idx):int(slice_start_idx + max_members)], slice_start_idx))

        return cls.__all_groups
    

    @classmethod
    def __set_total_priority(cls, priority: int) -> None:
        cls.total_priority += priority


    def _identify_common_item(self) -> None:
        _tmp_common_items = []
        _last_common = []

        for idx, rucksack in enumerate(self.rucksacks):
           #print(f'Last Common: {_last_common}')
            if idx == 0:
                _last_common = rucksack.all_items
                continue

            for ltr in rucksack.all_items:
                if ltr in _last_common and ltr not in _tmp_common_items:
                    _tmp_common_items.append(ltr.strip('\n'))
                    #print(f'Temp Common: {_tmp_common_items}')

            _last_common = _tmp_common_items
            _tmp_common_items = []

        self.common_items = _last_common

        #print(f'{self.group_id} - Common Items: {self.common_items}')
    

    def _set_priority(self) -> None:
        for item in self.common_items:
            self.priority += Rucksack.priorities[item]

        #print(f'\tPriority: {self.priority}')

    def __init__(self, rucksacks: list[Rucksack], group_id: int) -> None:
        self.group_id = group_id
        self.rucksacks = rucksacks
        self.common_items = []
        self.priority: int = 0
        
        self._identify_common_item()
        self._set_priority()

        ElfGroup.__set_total_priority(self.priority)


### Main ###
#priorities = build_priorities_list()

if len(sys.argv) < 2:
    raise RuntimeError('ERROR: Missing input file')

Rucksack.build_priorities_list()
rucksacks = []

with open(sys.argv[1]) as f:
    for line in f:
        this_rucksack = Rucksack(line.strip('\n'))
        rucksacks.append(this_rucksack)
        #print(f'Common items in this rucksack are: {this_rucksack.common_items}')
        #print(f'Their total priority is: {this_rucksack.priority}')

print(f'The total of all Rucksack priorities is: {Rucksack.total_priorities}')

elf_groups = ElfGroup.make_groups(rucksacks,3)

print(f'The total priority of all Elf Groups is: {ElfGroup.total_priority}')