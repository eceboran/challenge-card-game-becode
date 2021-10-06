from random import choice
from typing import List


class Player:
    """
    A class to represent a player
    ...
    Attributes
    ----------
    name : str
        name of the player
    cards: List['Card']
        list of cards the player has in their hand
    turn_count : int
        number of the current turn
    number_of_cards : int
        number of cards that the player has
    history : List['Card']
        list of all cards played by the player in previous turns

    Methods
    -------
    play()
        Returns a randomly picked card from the player's hand
    draw_single_card(drawn_card: List["Card"])
        Adds a card to the player's hand
    """

    def __init__(self, name: str, isHuman: bool):
        """
        Initializes an instance of the class Player
        :param name: A string for the name of the player
        :param isHuman: A boolean that is True for human players
        """
        # Assign the name of the player
        self.name = name
        self.isHuman = isHuman
        # Initialize the attributes cards, turn_count, number_of_cards and history
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def __str__(self):
        """
        Prints the name of the player and the number of cards they have
        """
        return f"Player {self.name} (currently has {self.number_of_cards} cards)"

    def play(self, played_card: 'Card' = None) -> "Card":
        """
        Returns a randomly picked card from the player's hand
        :return: An instance of Card to be played
        """
        if played_card is None:
            played_card = choice(self.cards)  # randomly select a card from cards
        self.cards.remove(played_card)  # remove the selected card from cards
        self.turn_count += 1  # increment the turn count
        self.number_of_cards -= 1  # decrement the number of cards
        self.history.append(
            played_card
        )  # append the card to the history of played cards
        print(f"{self.name} {self.turn_count} played: {played_card.__str__()}")
        return played_card

    def draw_single_card(self, drawn_card: List["Card"]):
        """
        Adds a card to the player's hand
        :param drawn_card: An instance of Card for the card drawn
        """
        if drawn_card is not None:
            self.cards.append(drawn_card)
            self.number_of_cards += 1  # increment the number of cards
