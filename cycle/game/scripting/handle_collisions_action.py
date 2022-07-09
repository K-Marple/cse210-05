import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionAction(Action):
    """An update action that handles interactions between the actors .
    
    The responsibility of HandleCollisionAction is to handle the situation when one snake collides
    with another snake, or a snake collides with itself, or the game is over.
    
    Attributes:
        _is_game_over (bool): whether or not the game is over.
    """

    def __init__(self):
        """Contructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.
        
        Args:
            cast (Cast): the cast of Actors in the game.
            script (Script): the script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_player_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score and moves the food if a snake collides with it.
        
        Args:
            cast (Cast): the cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        player1_snake = cast.get_first_actor("player1")
        player2_snake = cast.get_first_actor("player2")
        head1 = player1_snake.get_head()
        head2 = player2_snake.get_head()

        if head1.get_position().equals(food.get_position()):
            points = food.get_points()
            player1_snake.grow_tail(points)
            score.add_points(points)
            food.reset()
        elif head2.get_position().equals(food.get_position()):
            points = food.get_points()
            player2_snake.grow_tail(points)
            score.add_points()
            food.reset()

    def _handle_player_collision(self, cast):
        """Updates the score if the snakes collide with each other.
        
        Args:
            cast (Cast): the cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        player1_snake = cast.get_first_actor("player1")
        player2_snake = cast.get_first_actor("player2")
        head1 = player1_snake.get_head()
        head2 = player2_snake.get_head()
        segments1 = player1_snake.get_segments()[1:]
        segments2 = player2_snake.get_segments()[1:]

        for segment in segments1:
            if head2.get_position().equals(segment.get_position()):
                points = score.get_points()
                player1_snake.grow_tail(points)
                score.add_points(points)

        for segment in segments2:
            if head1.get_position().equals(segment.get_position()):
                points = score.get_points()
                player2_snake.grow_tail(points)
                score.add_points(points)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a snake collides with itself.
        
        Args:
            cast (Cast): the cast of Actors in the game.
        """
        snake = cast.get_first_actor("player1")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]

        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snakes white if the game is over.
        
        Args:
            cast (Cast): the cast of Actors in the game.
        """
        if self._is_game_over:
            player1_snake = cast.get_first_actor("player1")
            player2_snake = cast.get_first_actor("player2")
            segments1 = player1_snake.get_segments()
            segments2 = player2_snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1 and segments2:
                segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)