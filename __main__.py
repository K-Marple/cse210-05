import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.cycle import Cycle

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionAction
from game.scripting.draw_actors_action import DrawActorsAction

from game.directing.director import Director

from game.services.keyboard import Keyboard
from game.services.video import Video

from game.shared.color import Color
from game.shared.point import Point


def main():

    # create the cast
    cast = Cast()
    cast.add_actor("player1", Cycle())
    cast.add_actor("player2", Cycle())
    cast.add_actor("scores", Score())

    # start the game
    keyboard = Keyboard()
    video = Video()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionAction())
    script.add_action("output", DrawActorsAction(video))

    director = Director(video)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()