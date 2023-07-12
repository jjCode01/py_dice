# Py_Dice_Throw

Small program to model throwing dice and tracking their movements.  
Movements will follow the pattern of numbers on the dice based on the starting (face up) number and direction it is thrown. As the dice rolls the program simulates random changes in direction, which decreases as the strength of the throw increases.

## Parameters

There are 2 optional paramaters that can be set when rolling the dice:
 * `shake` - Default is `False`. Pass `True` to mimic shaking the dice in you hand before throwing them. This just sets each dice to a random value (1-6).
 * `strength` - Default will be a random number between 1 and 20. Pass any positive integer to mimic how hard the dice are thrown. The strength value is how may times the dice will roll to a new face.

## Usage

```python

dice = Dice(5) # Initialize with 5 dice.
dice.roll(shake=True, strength=10) # Roll the dice
print(dice) # print the current values of all the dice (facing up)

for die in dice.dice:
    print(die.moves) # show all the dice movements

```