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

    class SearchOrder(Enum):
        seed_to_soil = 0
        soil_to_fertilizer = 1
        fertilizer_to_water = 2
        water_to_light = 3
        light_to_temperature = 4
        temperature_to_humidity = 5
        humidity_to_location = 6


    # Notice parameter is "mappings" (plural)
    def _define_mappings(self, map_type: str, mappings: List[int]) -> None:
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

        self.mappings[map_type] = []
        
        source, destination = map_type.split('_to_')
        self.source_ranges[source] = []
        self.destination_ranges[destination] = []

        for _slice in _get_slices(len(mappings)):
            # print(f'\tData slice = {mappings[_slice]}')
            src_range, dst_range = _get_ranges(mappings[_slice])
            self.mappings[map_type].append((src_range, dst_range))
            self.source_ranges[source].append(src_range)
            self.destination_ranges[destination].append(dst_range)

    def _get_seed_ranges(self) -> List[range]:
        sr = []

        for r in range(int(len(self.seeds_list) / 2)):
            start = self.seeds_list[2*r]
            end = start + self.seeds_list[2*r + 1]
            sr.append(range(start, end))
        
        return sr

    def input(self, string: str) -> None:
        k,v = string.strip().split(':')
        v_int_list = [int(n) for n in v.strip().split(' ')]

        if k.lower() == 'seeds':
            self.seeds_list = v_int_list
            self.seed_ranges = self._get_seed_ranges()

            print(f'Seed Ranges: {self.seed_ranges}')

        if ' map' in k.lower():
            map_type = k.split(' ')[0]
            map_type = map_type.replace('-', '_')
            self._define_mappings(map_type, v_int_list)
    
    def map_seeds(self) -> None:
        for seed in self.seeds_list:
            print(f'Mapping Seed #:{seed}')
            seed_map_row = [seed]

            for search in self.SearchOrder:
                # print(f'\t\tSearching... {search.name}')
                mapping = self.mappings[search.name]
                # print(f'\t\tZip Mapping = {mapping}')
                src_value = seed_map_row[search.value]
                dst_value: int = None
                srcIdx: int = None

                for map in mapping:
                    # print(f'\t\tRange Map: {map}')
                    if src_value in map[0]:
                        srcIdx = map[0].index(src_value)
                        dst_value = map[1][srcIdx]
                        break

                if dst_value is None: dst_value = src_value

                seed_map_row.append(dst_value)

            self.seed_map.append(seed_map_row)
        
    def show_seed_map(self) -> None:
        # pass
        for _ in self.seed_map: print(_)

    def get_locations(self) -> None:
        locations = []

        for mapping in self.seed_map:
            locations.append(mapping[-1])

        locations.sort()
        print(f'Locations: {locations}')

    def __init__(self) -> None:
        self.seeds_list = []
        self.seed_ranges = []
        self.seed_map = []
        self.mappings = {}
        self.source_ranges = {}
        self.destination_ranges = {}

    def __str__(self) -> str:
        return f'Mappings: {self.mappings}'

    def __repr__(self
    ) -> str:
        pass




### Call Main ###
if __name__ == '__main__':
    print('\nImport this file as a module\n')