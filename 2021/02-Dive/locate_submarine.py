import sys

class Submarine():
    def add_maneuver(self, direction: str, distance: int) -> None:
        self.maneuvers.append(dict(direction = direction, distance = int(distance)))

    def __init__(self) -> None:
        self.maneuvers = []
        self.h_location = 0
        self.v_location = 0

class Submarine01(Submarine):
    def execute_maneuvers(self) -> None:
        for maneuver in self.maneuvers:
            if maneuver['direction'] == 'forward': self.h_location += maneuver['distance']
            if maneuver['direction'] == 'down': self.v_location += maneuver['distance']
            if maneuver['direction'] == 'up': self.v_location -= maneuver['distance']

    def add_maneuver(self, direction: str, distance: int) -> None:
        return super().add_maneuver(direction, distance)
    
    def __init__(self) -> None:
        super().__init__()

class Submarine02(Submarine):
    def execute_maneuvers(self) -> None:
        for maneuver in self.maneuvers:
            if maneuver['direction'] == 'down': self.aim += maneuver['distance']
            if maneuver['direction'] == 'up': self.aim -= maneuver['distance']
            if maneuver['direction'] == 'forward':
                self.h_location += maneuver['distance']
                self.v_location = self.v_location + self.aim * maneuver['distance']


    def add_maneuver(self, direction: str, distance: int) -> None:
        return super().add_maneuver(direction, distance)

    def __init__(self) -> None:
        super().__init__()
        self.aim = 0

def main () -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')
    
    submarine = Submarine02()

    with open(sys.argv[1]) as f:
        for line in f:
            line.strip('\n')
            direction, distance = line.split()
            submarine.add_maneuver(direction, int(distance))
    
    #print(f'Submarine Maneuvers: {submarine.maneuvers}')
    submarine.execute_maneuvers()
    print(f'H_Location = {submarine.h_location}  V_Location = {submarine.v_location}')
    print(f'Product = {submarine.h_location * submarine.v_location}')
    



### Call Main ###
if __name__ == '__main__':
    main()