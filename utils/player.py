from random import choice as choice


class Player:
    """
        A class to represent a player.
        ...
        Attributes
        ----------
        name : str
            name of the player
        cards: List['Card']
            list of cards the player has in their hand
        turn_count : int
            number of the last turn played by the player
        number_of_cards : int
            number of cards that the player has
        history : List['Card']
            list of all cards played by the player in previous turns

        Methods
        -------
        play(icon: str)
            Assigns the correct color to the symbol
    """

    def __init__(self, name: str):
        """
            Initialize an instance of the class Player
            :param name: A string for the name of the player
        """
        # Assign the name of the player
        self.name = name
        # Initialize the attributes cards, turn_count, number_of_cards and history
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def __str__(self):
        """
        Print the name of the player and the number of cards they have
        """
        return f"Player {self.name} (currently has {self.number_of_cards} cards)"

    def play(self):
        """
            Returns a randomly picked card from the player's hand
            :return: An instance of the Card
        """
        random_card = choice(self.cards)
        self.cards.remove(random_card)
        self.turn_count += 1
        self.history.append(random_card)
        # print(f"{self.name} {self.turn_count} played: {random_card.value} {random_card.icon}")
        return random_card

    def draw(self, card):
        if card is not None:
            self.cards.append(card)
            # print(f"Player number {self.name} card {len(self.cards)}")
