from random import choice

class Player:
    """
        A class to represent a player.
        ...
        Attributes
        ----------
        cards : List[Card]
            color of the symbol
        turn_count : str
            icon of the symbol
        number_of_cards
            xxx
        history
            xxx
    """

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play(self):
        """
            xx
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