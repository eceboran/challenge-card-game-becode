from typing import List


class Symbol:
    """
    A class to represent a playing card symbol
    ...
    Attributes
    ----------
    icon : str
        icon of the symbol (♥, ♦, ♣, or ♠) (unicode: ["\u2665","\u2666","\u2663","\u2660"])
    color : str
        color of the symbol (red or black)

    Methods
    -------
    assign_color(icon: str)
        Assigns the correct color to the symbol
    """

    # A dictionary for the icon and color of suits in a traditional deck
    suits = dict(
        Diamonds={"Icon": "♦", "Color": "red"},
        Hearts={"Icon": "♥", "Color": "red"},
        Clubs={"Icon": "♣", "Color": "black"},
        Spades={"Icon": "♠", "Color": "black"},
    )

    def __init__(self, icon: str):
        """
        Initializes an instance of the class Symbol and assign the correct color to it
        :param icon: A string for the icon of the symbol from the list [♥, ♦, ♣, ♠]
        """
        # Assign attribute icon
        self.icon = icon
        # Assign the color (red or black) corresponding to the icon
        self.color = self.assign_color(self.icon)

    def __str__(self):
        """
        Prints the symbol and its color
        """
        return f"{self.icon} symbol ({self.color})"

    @classmethod
    def assign_color(cls, icon: str):
        """
        Assigns a color to the Symbol instance according to its icon
        :param icon: A string for the icon of the symbol
            from the list [♥, ♦, ♣, ♠]
        :return: A string for the color of the symbol (red or black)
        """
        color = [x["Color"] for x in cls.suits.values() if x["Icon"] == icon][0]
        return color


class Card(Symbol):
    """
    A class to represent a playing card. Inherits from class Symbol
    ...
    Attributes
    ----------
    value: str
        value of the symbol ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", or "K")
    icon : str
        icon of the symbol (♥, ♦, ♣, or ♠) (unicode: ["\u2665","\u2666","\u2663","\u2660"])
    color : str
        color of the symbol (red or black)

    Methods
    -------
    list_card_names(card_list: List['Card'])
        Returns a list of strings for the values and icons given a list of card instances
    """

    icons = [
        "♥",
        "♦",
        "♣",
        "♠",
    ]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, value: str, icon: str):
        """
        Initializes an instance of the class Card
        :param value: A string for the value of the symbol
            from the list ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", or "K"]
        :param icon: A string for the icon of the symbol
            from the list [♥, ♦, ♣, ♠]
        """
        # Generate a symbol
        super().__init__(icon)
        # Assign the value of the card
        self.value = value

    def __str__(self):
        """
        Prints the symbol value, icon and color
        """
        return f"{self.value}{self.icon}"

    @staticmethod
    def list_card_names(card_list: List["Card"]) -> list:
        """
        Returns a list of card names and icons from a list of cards
        :param card_list: An list of instances of Card
        :return: A list of strings with the same length as card_list
                 Elements are in the format "<card value><card icon>"
        """
        return [f"{x.value}{x.icon}" for x in card_list]
