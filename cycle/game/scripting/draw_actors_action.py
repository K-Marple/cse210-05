from game.scripting.action import Action


class DrawActorsAction(Action):
    """An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.
    
    Attributes:
        _video (Video): an instance of Video.
    """

    def __init__(self, video):
        """Constructs a new DrawActorsAction using the specified Video.
        
        Args:
            video (Video): an instance of Video.
        """
        self._video = video

    def execute(self, cast, script):
        """Executes the draw actors action.
        
        Args:
            cast (Cast): the cast of Actors in the game.
            script (Script): the script of Actions in the game.
        """
        score1, score2 = cast.get_actors("scores")
        food = cast.get_first_actor("foods")
        snakes = cast.get_actors("snakes")
        player1_snake = snakes[0]
        player2_snake = snakes[1]
        segments1 = player1_snake.get_segments()
        segments2 = player2_snake.get_segments()
        messages = cast.get_actors("messages")

        self._video.clear_buffer()
        self._video.draw_actor(food)
        self._video.draw_actors(segments1)
        self._video.draw_actors(segments2)
        self._video.draw_actor(score1)
        self._video.draw_actor(score2)
        self._video.draw_actors(messages, True)
        self._video.flush_buffer()
