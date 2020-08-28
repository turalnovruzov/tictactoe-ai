class Tictactoe:
    """
    Tictactoe contains the game model.
    All the function related to the game's structure is in this class.
    """

    def __init__(self):
        """
        Initializes a new Tictactoe game. Creates player and board.
        """
        # Constants
        self.X = 'X'
        self.O = 'O'

        # Current player
        self.player = X

        # Board
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
