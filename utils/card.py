class Symbol:
    """
        A class to represent a playing card symbol (suit).
        ...
        Attributes
        ----------
        color : str
            color of the symbol
        icon : str
            icon of the symbol
    """

    def __init__(self, color: str = None, icon: str = None):
        self.color = color
        self.icon = icon


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

    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value

