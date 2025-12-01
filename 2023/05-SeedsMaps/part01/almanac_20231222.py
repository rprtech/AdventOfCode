from enum import Enum
from typing import List, Tuple

class Almanac():
    class Map(Enum):
        SEED = 0
        SOIL = 1
        FERTILIZER = 2
        WATER = 3
        LIGHT = 4
        TEMPERATURE = 5
        HUMIDITY = 6
        LOCATION = 7

    # Notice parameter is "mappings" (plural)
    def _make_map(self, src: str, dst: str, mappings: List[int]) -> None:
        def _get_slices(data_length: int) -> List[slice]:
            slices = []

            for x in range(int(data_length/3)):
                start = 3*x
                end = start + 3
                slices.append(slice(start,end))
            
            return slices
        
        # Notice parameter is "mapping" (singular)
        def _get_ranges(mapping: List[int]) -> Tuple[range, range]:
            # drs = destination range start, srs = source range start, rl = range length
            drs, srs, rl = mapping
            return (range(srs, srs + rl), range(drs, drs + rl))

        print(f'Mapping: {src} to {dst}')

        def _resize_map() -> None:
            map_size = len(self.map)

            if map_size < larger_range:
                print(f'\tStart enlarging map')
                
                for _ in range(map_size, larger_range):
                    self.map.append([None] * (len(self.Map) - 1))

                print(f'\tFinished enlarging map')

        def _map_src_to_dst() -> None:
            for idxSrc, valDst in zip(src_range, dst_range):
                # print(f'\t\tSource Destination Mapping: {mapSrcDst}')
                # srcIdx, dstVal = mapSrcDst
                # print(f'\t\t{src.upper()}: {idxSrc} => {dst.upper()} : {valDst}')
                self.map[idxSrc][self.Map[src.upper()].value] = valDst

        def _finalize_map() -> None:
            for row in range(len(self.map)):
                for col in range(len(self.Map) - 1):
                    if self.map[row][col] is None: self.map[row][col] = row

        for _slice in _get_slices(len(mappings)):
            print(f'\tData slice = {mappings[_slice]}')
            src_range, dst_range = _get_ranges(mappings[_slice])
            larger_range = src_range[-1] + 1 if src_range[-1] > dst_range[-1] else dst_range[-1] + 1
            _resize_map()
            _map_src_to_dst()
            _finalize_map()
            # print(f'intSource = {list(src_range)}')
            # print(f'\tDestination = {list(dst_range)}')

    def input(self, string: str) -> None:
        k,v = string.strip().split(':')
        v_int_list = [int(n) for n in v.strip().split(' ')]

        if k.lower() == 'seeds': self.seeds_list = v_int_list

        if ' map' in k.lower():
            map_type = k.split(' ')[0]
            source, destination = map_type.split('-to-')
            self._make_map(source, destination, v_int_list)
    
    def show_map(self) -> None:
        for idx in range(len(self.map)): print(f'{idx} ==> {" ".join([str(_) for _ in self.map[idx]])}')

    def make_seed_map(self) -> None:
        for seed in self.seeds_list:
            seed_map_row = [seed]
            row = seed

            for col in range(len(self.Map) - 1):
                row = self.map[row][col]
                seed_map_row.append(row)

            self.seed_map.append(seed_map_row)
        
    def show_seed_map(self) -> None:
        for _ in self.seed_map: print(_)

    def get_locations(self) -> None:
        locations = []

        for mapping in self.seed_map:
            locations.append(mapping[-1])

        locations.sort()
        print(f'Locations: {locations}')

    def __init__(self) -> None:
        self.seeds_list = []
        self.map = []
        self.seed_map = []

    def __str__(self) -> str:
        return f'Map: {self.seeds_list}'

    def __repr__(self
    ) -> str:
        pass




### Call Main ###
if __name__ == '__main__':
    print('\nImport this file as a module\n')