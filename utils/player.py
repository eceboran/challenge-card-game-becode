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

    def __init__(self, name, cards=[], turn_count=0, number_of_cards=0, history=[]):
        self.name = name
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

    def play(self):
        """
            xx
        """
        random_card = random.choice(self.cards)
        self.turn_count += 1
        self.history.append(random_card)
        print(f"{self.name} {self.turn_count} played: {self.turn_count} {random_card.icon}")
        return random_card

    def draw(self, card):
        if card is not None:
            self.cards.append(card)
