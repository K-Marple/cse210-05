import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """The responsibility of Cycle is to move itself.
    
    Attributes:
        _points (int): the number of points the collision is worth.
    """

    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        """Gets the segments of the snakes."""
        return self._segments

    def move_next(self):
        """Moves the snakes segments and updates their velocities."""
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # updates velocities
        for i in range(len(self._segments) -1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Gets the snake's head."""
        return self._segments[0]

    def grow_tail(self, number_of_segments, color):
        """Grows the tails of the snakes everytime they change directions."""
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """Turns the head of the snake."""
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self):
        """Creates the body of the snake."""
        x = int(constants.MAX_X / 2)
        y1 = int((constants.MAX_Y / 2) - 40)
        y2 = int((constants.MAX_Y / 2) + 40)

        for i in range(constants.SNAKE_LENGTH):
            position1 = Point(x - i * constants.CELL_SIZE, y1)
            velocity1 = Point(1 * constants.CELL_SIZE, 0)
            text1 = "8" if i == 0 else "#"
            color1 = constants.YELLOW if i == 0 else constants.GREEN

            segment1 = Actor()
            segment1.set_position(position1)
            segment1.set_velocity(velocity1)
            segment1.set_text(text1)
            segment1.set_color(color1)
            self._segments.append(segment1)

        for j in range(constants.SNAKE_LENGTH):
            position2 = Point(x - j * constants.CELL_SIZE, y2)
            velocity2 = Point(1 * constants.CELL_SIZE, 0)
            text2 = "8" if i == 0 else "#"
            color2 = constants.PURPLE if j == 0 else constants.BLUE

            segment2 = Actor()
            segment2.set_position(position2)
            segment2.set_velocity(velocity2)
            segment2.set_text(text2)
            segment2.set_color(color2)
            self._segments.append(segment2)