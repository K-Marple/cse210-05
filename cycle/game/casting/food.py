import constants
from random import randint
from game.casting.actor import Actor
from game.shared.point import Point


class Food(Actor):
    """A tasty item that snakes eat.
    
    The responsibility of Food is to select a random position and points that it's worth.
    
    Attributes:
        _points (int): the number of points the food is worth.
    """

    def __init__(self):
        """Constructs a new Food."""
        super().__init__()
        self._points = 0
        self.reset()
        
    def reset(self):
        """Selects random points that the food is worth."""
        self._points = randint(1, 8)

    def get_points(self):
        """Gets teh points the food is worth.
        
        Returns:
            points (int): the points the food is worth.
        """
        return self._points


# turn food into collision points. needs to reset but not a 
# position reset just a points reset.