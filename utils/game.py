from utils import deck
from utils import card

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

    def __init__(self, players):
        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        current_deck = deck.Deck()
        current_deck.shuffle()
        current_deck.distribute(self.players)
        # Players play one card per turn, until they have no cards left
        for turn in range(len(self.players[0].cards)):
            self.turn_count += 1
            self.active_cards = []
            for current_player in self.players:
                played_card = current_player.play()
                print(f"{current_player.name} played: {played_card.value} {played_card.icon}")
                self.active_cards.append(played_card)
                self.history_cards.append(played_card)
            # At the end of the turn, display a message
            print(f"At turn {self.turn_count}, the active cards:")
            print(card.Card.list_card_names(self.active_cards))
            print(f"Total number of cards played: {len(self.history_cards)}")