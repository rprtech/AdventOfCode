import sys
from typing import List

class Crates:
    def top_crates_string(self) -> str:
        return ''.join(map(str, self.top_crates()))


    def top_crates(self) -> List[str]:
        top = []

        for crate in self.crates:
            top.append(crate[-1] if len(crate) != 0 else ' ')

        return top


    def __init__(self, *args) -> None:
        self.crates = []

        for arg in args:
            self.crates.append(list(arg))
    
        #print(f'New Set of Crates created: {self.stacks}')
        #print(f'The number of crate stacks are: {len(self.stacks)}')

    def __str__(self) -> str:
        return 'Not yet implemented!'

class Crane:
    def add_operation(self, num_crates: int, from_stack: int, to_stack: int):
        self.operations.append(dict(num_crates = int(num_crates), from_stack = int(from_stack), to_stack = int(to_stack)))

    def __init__(self, num_crates: int = 0, from_stack: int = 0, to_stack: int = 0) -> None:
        self.operations = []
        if (0, 0, 0) != (num_crates, from_stack, to_stack): self.add_operation(num_crates, from_stack, to_stack)

class CraneMover9000(Crane):
    def __init__(self, num_crates: int = 0, from_stack: int = 0, to_stack: int = 0) -> None:
        super().__init__(num_crates, from_stack, to_stack)

    def move(self, stacks: Crates, verbose: bool = False) -> Crates:
        for operation in self.operations:
            num_crates = operation['num_crates']
            src = operation['from_stack']
            dst = operation['to_stack']

            if verbose:
                print(f'Moving {num_crates} crates from stack-{src} to stack-{dst}')
                print(f'Before  -> {stacks.top_crates_string()}')
            
            for i in range(num_crates):
                stacks.crates[dst].append(stacks.crates[src].pop())
                if verbose: print(f'After {i+1} -> {stacks.top_crates_string()}')

        return stacks

class CraneMover9001(Crane):
    def __init__(self, num_crates: int = 0, from_stack: int = 0, to_stack: int = 0) -> None:
        super().__init__(num_crates, from_stack, to_stack)

    def move(self, stacks: Crates, verbose: bool = False) -> Crates:
        for operation in self.operations:
            num_crates = operation['num_crates']
            src = operation['from_stack']
            dst = operation['to_stack']

            if verbose:
                print(f'Moving {num_crates} crates from stack-{src} to stack-{dst}')
                print(f'Before  -> {stacks.top_crates_string()}')

            num_crates  *= -1
            stacks.crates[dst] = stacks.crates[dst] + stacks.crates[src][num_crates:]
            del stacks.crates[src][num_crates:]

            if verbose: print(f'After  -> {stacks.top_crates_string()}')

        return stacks



def main():
    supply_stacks = Crates("","RNPG","TJBLCSVH","TDBMNL","RVPSB","GCQSWMVH","WQSCDBJ","FQL","WMHTDLFV","LPBVMJF")

    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    #giant_crane = CraneMover9000()
    giant_crane = CraneMover9001()

    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip('\n').split()
            if 'move' not in line: continue
            giant_crane.add_operation(line[1], line[3], line[5])

    print(f'Original Stack\n{supply_stacks.top_crates_string()}')

    giant_crane.move(supply_stacks)
    
    print(f'Rearranged Stack\n{supply_stacks.top_crates_string()}')
    print(f'Supply Stacks: {supply_stacks}')




### Call Main ###
if __name__ == '__main__':
    main()