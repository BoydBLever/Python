from classes.ninja import Ninja
from classes.pirate import Pirate

coding_ninja = Ninja("coding_ninja")

black_beard = Pirate("black_beard")

black_beard.attack(coding_ninja)
coding_ninja.attack(black_beard).attack(black_beard).attack(black_beard)
