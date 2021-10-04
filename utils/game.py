class Board:
    """
        A class to represent the game board.
        ...
        Attributes
        ----------
        players : str
            color of the card
        turn_count : str
            icon of the card
        active_cards: str
            value of the card
    """

    def __init__(self):
        self.fill_deck()
        self.shuffle()
        for ii in range(0, 55):
            print(self.draw())

    def start_game(self, Players):
        print(1)