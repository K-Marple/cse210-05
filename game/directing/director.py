class Director:
    """A person who directs the game.
    
    The responsibility of Director is to control the steps of the game.
    
    Attributes:
        _video (Video): for providing video output.
    """

    def __init__(self, video):
        """Constructs a new Director using the specified video service.
        
        Args:
            video (Video): an instance of Video.
        """
        self._video = video

    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.
        
        Args:
            cast (Cast): the cast of actors.
            script (Script): the script of actions.
        """
        self._video.open_window()
        while self._video.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        self._video.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (str): the action group name.
            cast (Cast): the cast of actors.
            script (Script): the script of actions.
        """
        actions = script.get_actions(group)
        for action in actions:
            action.execute(cast, script)