class Symbol:
    """
    A class to represent a playing card symbol.
    ...
    Attributes
    ----------
    color : str
        color of the symbol (red or black)
    icon : str
        icon of the symbol (♥, ♦, ♣, or ♠) (unicode: ["\u2665","\u2666","\u2663","\u2660"])
    """

    # A dictionary of suits in a deck
    suits = dict(
        Diamonds={"Icon": "♦", "Color": "red"},
        Hearts={"Icon": "♥", "Color": "red"},
        Clubs={"Icon": "♣", "Color": "black"},
        Spades={"Icon": "♠", "Color": "black"},
    )

    def __init__(self, icon: str = None):
        """
        Initialize an instance of Symbol and assign a color to it
        Arguments:
        :param icon: a string for the icon of the symbol from the list [♥, ♦, ♣, ♠]

        """
        # Assign attribute icon
        self.icon = icon
        # Assign the color (red or black) corresponding to the icon
        self.assign_color()

    def __str__(self):
        """
        Print the symbol and its color
        """
        return f"{self.icon} symbol ({self.color})".capitalize()

    def assign_color(self):
        """
        Assign a color to the Symbol instance according to its icon
        """
        color = [x["Color"] for x in Symbol.suits.values() if x["Icon"] == self.icon][0]
        self.color = color


class Card(Symbol):
    """
        A class to represent a playing card.
        Inherits from class Symbol.
        ...
        Attributes
        ----------
        color : str
            color of the card
        icon : str
            icon of the card
        value: str
            value of the card
    """

    icons = [
        "♥",
        "♦",
        "♣",
        "♠",
    ]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, color, icon, value):
        super().__init__(icon)
        self.value = value

    @staticmethod
    def list_card_names(cards) -> list:
        return [f"{x.value}{x.icon}" for x in cards]
