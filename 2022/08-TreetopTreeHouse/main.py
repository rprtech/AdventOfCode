import sys
import math
from enum import Enum
from typing import Tuple, Dict, List

class Tree():
    @classmethod
    def get_trees(cls, trees: Tuple) -> Tuple:
        for r, rows in enumerate(trees):
            for c, tree in enumerate(rows):
                yield (tree, r, c)

    @classmethod
    def discover_neighbors(cls, trees: Tuple) -> None:
        max_rc = len(trees) - 1
        
        for tree, r, c in cls.get_trees(trees):
            #print(f'Row: {r}, Col: {c},  Tree: {tree.__dict__}')
            left = trees[r][c-1] if c > 0 else None
            right = trees[r][c+1] if c < max_rc else None
            top = trees[r-1][c] if r > 0 else None
            bottom = trees[r+1][c] if r < max_rc else None
            tree._assign_neighbors(left, right, top, bottom)

    @classmethod
    def get_scenic_scores(cls, trees: Tuple) -> Tuple:
        scores = list()
        for tree, *_ in cls.get_trees(trees):
            tree._calculate_viewing_distance()
            scores.append(tree.scenic_score)

        scores.sort()
        return tuple(scores)

    def _calculate_viewing_distance(self) -> None:
        neighbor: Tree

        for direction, neighbor in self.neighbors.items():
            if neighbor is None: continue

            while neighbor is not None:
                self.viewing_distance[direction] += 1

                if neighbor.height >= self.height: break

                #print(f'Getting next neighbor {neighbor.__dict__}')
                neighbor = neighbor.neighbors[direction]
        
        self.scenic_score = math.prod(self.viewing_distance.values())
    
    def _assign_neighbors(self, left, right, top, bottom) -> None:
        self.neighbors = dict(left = left, right = right, top = top, bottom = bottom)
        # self._calculate_viewing_distance()

    def __init__(self, row: int, col: int, height: int) -> None:
        self.row = row
        self.col = col
        self.height = height
        self.neighbors: Dict
        self.viewing_distance = dict(left = 0, right = 0, top = 0, bottom = 0)
        self.scenic_score: int = 0

class Grid():
    @classmethod
    def new(cls, file_handle) -> Tuple:
        grid = list()

        for line in file_handle:
            line = line.strip('\n')
            grid.append(tuple(line))
    
        return Grid(tuple(grid))

    def _look(self, cell: Tuple, tallest: int) -> Tuple|None:
        r,c = cell
        return tuple([r,c]) if int(self.layout[r][c]) > tallest else None
    
    def _get_cell_rc(self, i: int, j: int) -> Dict:
        """
        Left, right, top, and bottom is the location of the observer from outside the grid.
        It should be read as from <location> look <opposite location>.  Therefore:
        An observer on the left will look right, an oberver on the right will look left.
        An oberver on the top will look down, an observer on the bottom will look up.
        
        The third and fourth values are for the previous cell.  Remember when look left/right
        the column changes and when look top/bottom the row changes
        """
        return {"left": (int(i), int(j)),
                "right": (int(i), int(self.max_rc - j)),
                "top": (int(j), int(i)),
                "bottom": (int(row := self.max_rc - j), int(i))
        }
    
    def _get_visible(self) -> int:
        visible = list()
        for i in range(len(self.layout)):
            previous_tallest = dict(left = int(self.layout[i][0]), \
                                    right = int(self.layout[i][self.max_rc]), \
                                    top = int(self.layout[0][i]), \
                                    bottom = int(self.layout[self.max_rc][i]))
            #print(f'\n\nI = {i}')

            for j in range(len(self.layout)):
                """
                This condition will allow the '*look*' functions to not have to each deal
                with layout boundaries
                """
                if i in (0, self.max_rc) or j in (0, self.max_rc):
                    visible.append(tuple([i,j]))
                    continue

                cell = self._get_cell_rc(i,j)

                for location,rc_value in cell.items():
                    #print(f'{location} = {rc_value}')
                    if (tallest := previous_tallest[location]) == self.max_height \
                        or (result := self._look(rc_value, tallest)) is None: continue

                    visible.append(result)
                    if result == (2,2): print(f'\tLocation = {location} Result = {result}')
                    r, c = result
                    previous_tallest[location] = int(self.layout[r][c])
                
                #print(f'\t\tPrevious_Tallest = {previous_tallest}')
        visible = list(set(visible))
        visible.sort()
        #print(f'\n\nVisible Trees:\n{visible}\n\n')
        return len(visible)

    def _make_trees(self) -> Tuple:
        trees = list()
        for r, rows in enumerate(self.layout):
            row = list()

            for c, height in enumerate(rows):
                row.append(Tree(r, c, height))
            
            #print(f'Row of trees: {row[1]}')
            trees.append(tuple(row))

        return tuple(trees)
    
    def __init__(self, layout) -> None:
        self.layout = layout
        self.max_rc = len(layout) - 1

        """
        USING LIST COMPREHENSION
        Create a list '[]' of the maximum value contained in each row of the layout.
        Then, get the maximum value from that resulting list
        """
        #self.max_height = max([max([col for col in row]) for row in self.layout])
        self.max_height = max([max(row) for row in self.layout])
        self.visible = self._get_visible()
        self.trees: List[Tree] = self._make_trees()

        Tree.discover_neighbors(self.trees)

        self.all_scenic_scores = Tree.get_scenic_scores(self.trees)


def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    with open(sys.argv[1]) as f:
        grid: Grid = Grid.new(f)
    
    print(f'Num Row: {len(grid.layout)}, MAX_RC: {grid.max_rc}')
    #print(f'Layout = {grid.layout}')
    print(f'Max Height = {grid.max_height}')
    print(f'Number of trees visible from outside = {grid.visible}')
    print(f'Trees {isinstance(grid.trees, Tuple)}')
    print(f'Best Scenic Score: {max(grid.all_scenic_scores)}')



### Call Main ###
if __name__ == '__main__':
    main()