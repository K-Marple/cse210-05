import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.
    
    Attributes:
        _keyboard (Keyboard): an instance of Keyboard.
    """

    def __init__(self, keyboard):
        """Constructs a new ControlActorsAction using the specified Keyboard.
        
        Args:
            keyboard (Keyboard): an instance of Keyboard.
        """
        self._keyboard = keyboard
        self._direction1 = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.
        
        Args:
            cast (Cast): the cast of Actors in the game.
            script (Script): the script of Actions in the game.
        """
        snakes = cast.get_actors("snakes")

        # for player 1
        # left
        if self._keyboard.is_key_down("a"):
            self._direction1 = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard.is_key_down("d"):
            self._direction1 = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard.is_key_down("w"):
            self._direction1 = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard.is_key_down("s"):
            self._direction1 = Point(0, constants.CELL_SIZE)

        player1_snake = snakes[0]
        player1_snake.turn_head(self._direction1)

        snakes = cast.get_actors("snakes")

        # for player 2
        # left
        if self._keyboard.is_key_down("j"):
            self._direction2 = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard.is_key_down("l"):
            self._direction2 = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard.is_key_down("i"):
            self._direction2 = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard.is_key_down("k"):
            self._direction2 = Point(0, constants.CELL_SIZE)

        player2_snake = snakes[1]
        player2_snake.turn_head(self._direction2)