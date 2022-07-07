class Action:
    """A thing that is done. The responsibility of action is to do something that is integral or important
    in the game. Thus, it has one method, execute(), which should be overridden by the derived classes."""

    def execute(self, cast, script):
        """Executes something that is important to the game. This method should be overridden 
        by the dervided classes.
        
        Args:
            cast (Cast): the cast of Actors in the game.
            script (Script): the script of Actions in the game.
        """
        pass