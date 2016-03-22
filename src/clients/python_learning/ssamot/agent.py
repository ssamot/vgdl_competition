from ontology import *

class Agent:

     def __init__(self, logger):

        """
        The agent is created when playing in a new game starts.
        :param Reference to a file where logs can be written.
        :return: None.
        """
        pass


     def init(self, game, avatar, remMillis):

        """
        This function is called when each game is started.
        :param game Information about the game.
        :param avatar Information about the avatar.
        :param remMillis Number of milliseconds when this function is due to finish.
        :return: None.
        """
        pass


     def act(self, game, avatar, remMillis):

        """
        This function is called at every game cycle of a given game.
        :param game Information about the game.
        :param avatar Information about the avatar.
        :param remMillis Number of milliseconds when this function is due to finish.
        :return: The ACTION (one from the ones defined in avatar.actionList) to apply in the game this cycle.
        """
        pass


     def end(self, game, avatar, remMillis):

        """
        This function is called when a game has finished.
        :param game Information about the game.
        :param avatar Information about the avatar.
        :param remMillis Number of milliseconds when this function is due to finish.
        :return: None.
        """
        pass

