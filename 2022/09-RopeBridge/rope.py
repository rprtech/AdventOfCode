from typing import Tuple, List

class Knot:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x: int = x
        self.y: int = y
        self.history: List = []

    def move_r(self) -> Tuple[int]:
        self.x += 1
        return self.x, self.y

    def move_l(self) -> Tuple[int]:
        self.x -= 1
        return self.x, self.y

    def move_u(self) -> Tuple[int]:
        self.y += 1
        return self.x, self.y

    def move_d(self) -> Tuple[int]:
        self.y -= 1
        return self.x, self.y

    def follow(self, x: int, y: int) -> Tuple[int]:
        def deltaX() -> int:
            return x - self.x

        def deltaY() -> int:
            return y - self.y

        def no_move() -> Tuple[int]:
            return self.x, self.y

        # delta_x: int = x - self.x
        # delta_y: int = y - self.y

        if deltaX() == 2:
            self.move_r()
            self.move_u() if deltaY() > 0 else self.move_d() if deltaY() < 0 else no_move()
            # self.y += delta_y

        if deltaX() == -2:
            self.move_l()
            self.move_u() if deltaY() > 0 else self.move_d() if deltaY() < 0 else no_move()
            # self.y += delta_y

        if deltaY() == 2:
            self.move_u()
            self.move_r() if deltaX() > 0 else self.move_l() if deltaX() < 0 else no_move()
            # self.x += delta_x

        if deltaY() == -2:
            self.move_d()
            self.move_r() if deltaX() > 0 else self.move_l() if deltaX() < 0 else no_move()
            # self.x += delta_x

        return self.x, self.y

class Rope:
    def __init__(self, x: int = 0, y: int = 0, num_knots: int = 2) -> None:
        self.knots: List[Knot] = []

        for _ in range(num_knots):
            self.knots += [Knot(x=x, y=y)]

        self.head_knot = self.knots[0]
        self.tail_knot = self.knots[-1]

        

    def move(self, direction: str, distance: int, show: bool = False) -> List:
        direction = direction.upper()

        for _ in range(int(distance)):
            followX, followY = (None, None)

            for knot in self.knots:
                # Move the head knot (index 0)
                if followX is None and followY is None:
                    if direction == 'R': knot.history.append(knot.move_r())
                    if direction == 'L': knot.history.append(knot.move_l())
                    if direction == 'U': knot.history.append(knot.move_u())
                    if direction == 'D': knot.history.append(knot.move_d())

                    followX, followY = knot.history[-1]
                    continue

                # Other knots follow the previous knot
                knot.history.append(knot.follow(followX, followY))
                followX, followY = knot.history[-1]

            if show:
                for idx, knot in enumerate(self.knots):
                    print(f'\t[{idx}] => {knot.history[-1]}')
                print('\t=======================================')
            # if direction == 'R': self.head_knot.history.append(self.head_knot.move_r())
            # if direction == 'L': self.head_knot.history.append(self.head_knot.move_l())
            # if direction == 'U': self.head_knot.history.append(self.head_knot.move_u())
            # if direction == 'D': self.head_knot.history.append(self.head_knot.move_d())
            
            # hX, hY = self.head_knot.history[-1]

            # self.tail_knot.history.append(self.tail_knot.follow(hX,hY))

            # if show: print(f'\tHead = {self.head_knot.history[-1]}\n\tTail = {self.tail_knot.history[-1]}\n')
            
        return [knot.history[-1] for knot in self.knots]





### Call Main ###
# if __name__ == "__main__":
#     main()