import sys
from enum import Enum
from typing import Tuple

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Points(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

class Player:
    def __init__(self, play: Shape):
        self.play = play
        self.score: int = 0
        self.state: Points

class Game:
    def _assign_points(self) -> None:
        self.player1.score = self.player1.play.value + self.player1.state.value
        self.player2.score = self.player2.play.value + self.player2.state.value
    
    def _determine_winner(self) -> None:
        """
        Based on the values assigned to ROCK, PAPER, and SCISSORS in the Enum Shape class,
        adding 3 to the value of the play for player1 (example: ROCK + 3 = 4) then subtracting
        the value of the play for player2 (4 - PAPER = 2), and taking modulus base 3 of that
        difference would identify the winner!
        0: Both players made the same play so the result is a DRAW
        1: Player1's play beats player2's so player1 wins
        2: Player2's play beats player1's so player2 wins
        """

        p1 = self.player1.play
        p2 = self.player2.play

        result = (p1.value + 3 - p2.value) % 3
        #print(f'Mod 3 result is: {result}')

        if result == 1:
            #print(f'Player1 wins! {p1.name} beats {p2.name}')
            self.player1.state = Points.WIN
            self.player2.state = Points.LOSE
        elif result == 2:
            #print(f'Player2 wins! {p2.name} beats {p1.name}')
            self.player1.state = Points.LOSE
            self.player2.state = Points.WIN
        else:
            #print("Both played the same - A DRAW")
            self.player1.state = Points.DRAW
            self.player2.state = Points.DRAW

    def _set_plays(self, player1: Shape, player2: Shape) -> None:
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        
        self._determine_winner()
        self._assign_points()

    def _get_desired_outcome_play(self, play: Shape, desired_outcome: Points) -> Shape:
        outcome = {
            'rock': {
                'lose': Shape.SCISSORS,
                'draw': Shape.ROCK,
                'win': Shape.PAPER
            },
            'paper': {
                'lose': Shape.ROCK,
                'draw': Shape.PAPER,
                'win': Shape.SCISSORS
            },
            'scissors': {
                'lose': Shape.PAPER,
                'draw': Shape.SCISSORS,
                'win': Shape.ROCK
            }
        }

        #print(f'Play is: {play.name}')
        #print(f'The desired outcome is: {desired_outcome.name}')
        #print(f'The other player must play: {outcome[play.name.lower()][desired_outcome.name.lower()]}')
        
        return outcome[play.name.lower()][desired_outcome.name.lower()]
    
    def __init__(self, p1_input, p2_input) -> None:
        if isinstance(p1_input, Shape) and isinstance(p2_input, Shape):
            self._set_plays(p1_input, p2_input)
        elif isinstance(p1_input, Shape) and isinstance(p2_input, Points):
            p2_play = self._get_desired_outcome_play(p1_input, p2_input)
            self._set_plays(p1_input, p2_play)
        else:
            print(f'player1_input type is: {type(p1_input)}')
            print(f'player2_input type is: {type(p2_input)}')


def decode_play(cipher: str) -> Shape:
    decipher_play = {
        'a': Shape.ROCK,
        'x': Shape.ROCK,
        'b': Shape.PAPER,
        'y': Shape.PAPER,
        'c': Shape.SCISSORS,
        'z': Shape.SCISSORS
    }

    return decipher_play[cipher.lower()]

def decode_outcome(cipher: str) -> Points:
    decipher_outcome = {
        'x': Points.LOSE,
        'y': Points.DRAW,
        'z': Points.WIN
    }

    return decipher_outcome[cipher.lower()]

def total_points(games: list[Game]) -> Tuple[int, int]:
    player1_total = 0
    player2_total = 0

    for game in games:
        player1_total += game.player1.score
        player2_total += game.player2.score

    return player1_total, player2_total

### Main ###
if len(sys.argv) < 2:
    raise RuntimeError('ERROR: Missing input file')

games = []

with open(sys.argv[1]) as f:
    for line in f:
        player1_play, player2_outcome = line.split()
        p1 = decode_play(player1_play)
        p2 = decode_outcome(player2_outcome)
        games.append(Game(p1, p2))

#print(f'Number of games played: {len(games)}')

p1_total, p2_total = total_points(games)

print(f'Total points scored by player1 is: {p1_total}')
print(f'Total points scored by player2 is: {p2_total}')