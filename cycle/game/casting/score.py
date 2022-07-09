from game.casting.actor import Actor


class Score(Actor):
    """A record of points made or lost.
    
    The responsibility of Score is to keep track of the points the players have earned by hitting
    each other. It contains methods for adding and getting points. Client should use get_text() to 
    get a string representation of the points earned.
    
    Attributes:
        _points (int): the points earned in the game.
    """

    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): the points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

    def get_points(self):
        """Gets the points the collision is worth.
        
        Returns:
            points (int): the points the collision is worth.
        """
        return self._points