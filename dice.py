from random import randint


class Die:
    roll_matrix = [
        [
            [5, 3, 4, 2],  # up, right, left, down
            [6, 4, 3, 1],
            [6, 2, 5, 1],
            [6, 5, 2, 1],
            [6, 3, 4, 1],
            [2, 3, 4, 5],
        ],
        [
            [5, 3, 4, 2],
            [6, 4, 3, 1],
            [5, 6, 1, 2],
            [5, 1, 6, 2],
            [1, 4, 3, 6],
            [5, 4, 3, 2],
        ],
        [
            [4, 5, 2, 3],
            [4, 1, 6, 3],
            [6, 2, 5, 1],
            [1, 2, 5, 6],
            [4, 6, 1, 3],
            [4, 2, 5, 3],
        ],
        [
            [3, 2, 5, 4],
            [3, 6, 1, 4],
            [1, 5, 2, 6],
            [6, 5, 2, 1],
            [3, 1, 6, 4],
            [3, 5, 2, 4],
        ],
        [
            [2, 4, 3, 5],
            [1, 3, 4, 6],
            [2, 1, 6, 5],
            [2, 6, 1, 5],
            [6, 3, 4, 1],
            [2, 3, 4, 5],
        ],
        [
            [5, 3, 4, 2],
            [1, 3, 4, 6],
            [1, 5, 2, 6],
            [1, 2, 5, 6],
            [1, 4, 3, 6],
            [2, 3, 4, 5],
        ],
    ]

    def __init__(self, value: int = 1) -> None:
        self.value: int = value
        self.moves: list[int] = [value]

    def __eq__(self, __o: "Die") -> bool:
        return self.value == __o.value

    def __gt__(self, __o: "Die") -> bool:
        return self.value > __o.value
    
    def __hash__(self) -> int:
        return self.value

    def __lt__(self, __o: "Die") -> bool:
        return self.value < __o.value

    def __str__(self) -> str:
        return str(self.value)

    def shake(self):
        self.value = randint(1, 6)
        self.moves = [self.value]

    def roll(self, shake: bool = False, strength: int = 0):
        if shake:
            self.shake()

        self.moves = [self.value]
        direction: int = randint(0, 3)
        strength = randint(1, 20) if strength < 1 else strength
        edges = Die.roll_matrix[self.value - 1]

        for _ in range(strength):
            prev_val = self.value
            self.value = edges[self.value - 1][direction]
            self.moves.append(self.value)
            edges = Die.roll_matrix[prev_val - 1]
            direction = randint(1, 3) if _flip(strength // 5 + 1) else 0

class Dice:
    def __init__(self, count: int=1) -> None:
        if count < 1:
            raise ValueError("Count must be greater than 0!")
        
        self.dice: list[Die] = [Die() for _ in range(count)]

    def __len__(self) -> int:
        return len(self.dice)

    def __str__(self) -> str:
        return str([die.value for die in self.dice])
    
    @property
    def value(self) -> int:
        return sum(die.value for die in self.dice)

    def roll(self, shake: bool = False, strength: int = 0):
        strength = randint(1, 20) if strength < 1 else strength
        for die in self.dice:
            die.roll(shake=shake, strength=strength)

        
def _flip(odds: int) -> bool:
    if odds < 1:
        return False
    return randint(1, odds) == randint(1, odds)
