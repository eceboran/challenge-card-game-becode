from random import shuffle
from typing import List
from re import search
from utils import card


class Board:
    """
    A class to represent a board
    ...
    Attributes
    ----------
    players : List['Player']
        list of players
    turn_count: int
        number of the current turn
    active_cards : List['Card']
        list of last cards played by each player
    history_cards : List['Card']
        list of cards played since the start of the game (excluding active_cards)

    Methods
    -------
    start_game()
        Returns a randomly picked card from the player's hand
    """

    def __init__(self, players: List["Player"]):
        """
        Initializes an instance of the class Board
        :param players: A list of instances of Player for the players
        """
        # Assign the players
        self.players = players
        # Initialize the attributes turn_count, active_cards and history_cards
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def __str__(self):
        """
        Prints the number of cards each player has, and the number of cards played
        """
        return (
            f"The active cards are {*card.Card.list_card_names(self.active_cards),}"
            f"\n{len(self.history_cards)} cards played previously\n"
        )

    def start_game(self):
        """
        Starts the game
            Creates a new deck
            Shuffles the cards in the deck
            Distributes the cards to the players one by one
            Makes each player play one card in each turn, until there are no cards left
            In the end of each turn, displays
                the turn count
                the list of active cards
                the total number of cards previously played
        """
        # Create a new deck
        current_deck = Deck()
        # Shuffle the deck
        current_deck.shuffle()
        # Distribute the cards to the players one by one
        current_deck.distribute(self.players)
        # Players play one card per turn, until they have no cards left
        no_cards_per_player = self.players[0].number_of_cards
        no_turns = no_cards_per_player
        for current_turn in range(no_turns):
            self.turn_count += 1  # increment the turn count
            # Add the active cards from the previous turn to history and reset the active cards
            self.history_cards.extend(self.active_cards)
            self.active_cards = []
            # Each player plays a card
            for current_player in self.players:
                if current_player.isHuman:
                    # Display the active cars
                    print("Active cards:\n")
                    if len(self.active_cards) > 0:
                        card.Card.print_cards(self.active_cards)
                    # Display the player's cards
                    print("Your cards:\n")
                    card.Card.print_cards(current_player.cards)
                    selected_card_name = input("Choose a card to play: ")
                    # selected_card_name = "K of Hearts"
                    m = search("(?P<value>\w+) of (?P<icon>\w+)",selected_card_name)
                    selected_icon = m.group("icon")
                    selected_value = m.group("value")
                    if selected_icon.lower() == 'hearts':
                        selected_icon = "♥"
                    elif selected_icon.lower() == 'diamonds':
                        selected_icon = "♦"
                    elif selected_icon.lower() == 'clubs':
                        selected_icon = "♣"
                    elif selected_icon.lower() == 'spades':
                        selected_icon = "♠"
                    selected_card = [x for x in current_player.cards if (x.value == selected_value) & (x.icon == selected_icon)][0]
                    played_card = current_player.play(selected_card)  # card chosen by the player
                else:
                    played_card = current_player.play()  # card chosen by the computer
                self.active_cards.append(played_card)
            # At the end of the turn, display a message
            print(
                f"At turn {self.turn_count}, the active cards are:",
                *card.Card.list_card_names(self.active_cards),
                f"\nNumber of cards in history: {len(self.history_cards)}",
            )


class Deck:
    """
    A class to represent a deck of playing cards
    ...
    Attributes
    ----------
    cards: List['Card']
        list of cards in the deck

    color : str
        color of the symbol (red or black)

    Methods
    -------
    fill_deck()
        Creates a card for each combination of card value and icon and adds it to the deck
    shuffle()
        Shuffles the cards in the deck
    distribute(players: List["Player"])
        Distributes all cards to the players one by one
            Each player gets an equal number of cards
    draw_single_card()
        Draws a single card from the top of the deck (if there are any cards left)
    """

    def __init__(self):
        """
        Initialize an instance of the class Deck
        """
        # Construct and fill the deck
        self.fill_deck()

    def __str__(self):
        """
        Prints the number of cards in the deck
        """
        return f"There are {len(self.cards)} cards remaining in the deck"

    def fill_deck(self):
        """
        Creates a card for each combination of card value and icon and adds it to the deck
            card values: "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
            card icons: ♥, ♦, ♣, ♠
        """
        # The list of all possible card values and icons
        values = card.Card.values
        icons = card.Card.icons

        self.cards = []  # initialize an empty deck
        # For each value and icon combination, add a card to the deck
        for icon in icons:
            for value in values:
                self.cards.append(card.Card(value, icon))

    def shuffle(self):
        """
        Shuffles the cards in the deck
        """
        shuffle(self.cards)

    def distribute(self, players: List["Player"]):
        """
        Distributes all cards to the players one by one
            Each player gets an equal number of cards
        :param players: A list of instances of Player for the players
        """
        # Number of cards per player so that each player gets an equal number of cards
        no_players = len(players)
        no_cards_per_player = len(self.cards) // no_players

        for card_number in range(no_cards_per_player):
            for player_number in range(no_players):
                # Draw a card from the deck
                card_drawn = self.draw_single_card()
                # Add the card to the player's hand
                players[player_number].draw_single_card(card_drawn)

    def draw_single_card(self) -> "Card":
        """
        Draws a single card from the top of the deck (if there are any cards left)
        :return drawn_card: An instance of Card for the card drawn
                            None if there are no cards left
        """
        if len(self.cards) > 0:
            # Return the first card and remove it from the deck
            drawn_card = self.cards.pop(0)
        else:
            drawn_card = None
        return drawn_card
