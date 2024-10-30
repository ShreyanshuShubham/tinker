from enum import Enum, Flag, auto

class Color(Enum):
    RED: str = 'R'
    GREEN : str = 'G'
    BLUE : str = 'B'

# flag is enum type that support combination
# in a way union types
# combination is mathematically calculated therefore power of two like bit repr or can use auto
class Color2(Flag):
    RED : int = 1
    GREEN : int = 2
    BLUE : int = 4

green_and_blue : Color2 = Color2.GREEN | Color2.BLUE
print(green_and_blue)
print(green_and_blue.value)
print(Color2.RED in green_and_blue)
for c in green_and_blue:
    print(c)

# auto - auto assign int values for disticnt combination values
class Color3(Flag):
    RED : int = auto()
    GREEN : int = auto()
    BLUE : int = auto()