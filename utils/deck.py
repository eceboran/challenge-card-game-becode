from utils import card
from random import shuffle


class Deck:
    """
        A class to represent a deck.
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

    def __init__(self):
        self.fill_deck()

    def fill_deck(self):
        colors = ["red", "blue"]
        icons = [
            "♥",
            "♦",
            "♣",
            "♠",
        ]  # ["\u2665","\u2666","\u2663","\u2660","♥"] # ["♥", "♦", "♣", "♠"]
        values = "A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K".split(", ")

        self.cards = []
        for icon_number, icon in enumerate(icons):
            color = colors[icon_number // 2]
            for value in values:
                self.cards.append(card.Card(color, icon, value))

        # for mycard in self.cards:
        # print(mycard.icon + mycard.value)

    def shuffle(self):
        shuffle(self.cards)
        # for mycard in self.cards:
        # print(mycard.icon + mycard.value)

    def draw(self):
        """
            Draw a single card from the deck.
        """
        if len(self.cards) > 0:
            return self.cards.pop(
                0
            )  # Return the first card and remove it from the deck
        else:
            return None

    def distribute(self, Players, deal_size: int = 0):
        """
            Distribute cards to the players.
            As long as there are cards left.
        """
        # If the deal size is specified as 0 or not specified, distribute all cards to the players
        if deal_size == 0:
            deal_size = len(self.cards) // len(Players)

        for card_in_deal in range(deal_size):
            for player in range(len(Players)):
                # Draw a card from the deck
                card_drawn = self.draw()
                # Add the card to the player's hand
                Players[player].draw(card_drawn)
