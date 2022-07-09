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
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute_player1(self, cast, script):
        """Executes the control actors action.
        
        Args:
            cast (Cast): the cast of Actors in the game.
            script (Script): the script of Actions in the game.
        """
        # left
        if self._keyboard.is_key_down("a"):
            self._direction = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard.is_key_down("d"):
            self._direction = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard.is_key_down("w"):
            self._direction = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard.is_key_down("s"):
            self._direction = Point(0, constants.CELL_SIZE)

        player1_snake = cast.get_first_actor("player1")
        player1_snake.turn_head(self._direction)

    def execute_player2(self, cast, script):
        """Executes the control actors action.
        
        Args:
            cast (Cast): the cast of Actors in the game.
            script (Script): the script of Actions in the game.
        """
        # left
        if self._keyboard.is_key_down("j"):
            self._direction = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard.is_key_down("l"):
            self._direction = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard.is_key_down("i"):
            self._direction = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard.is_key_down("k"):
            self._direction = Point(0, constants.CELL_SIZE)

        player2_snake = cast.get_first_actor("player2")
        player2_snake.turn_head(self._direction)