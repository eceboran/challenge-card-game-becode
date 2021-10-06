from utils import player
from utils import game
from utils import card

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("hi")

    # Define the player names
    player_names = ["A", "B", "C", "D"]

    # Create players
    players = []
    for player_name in player_names:
        players.append(player.Player(player_name))

    # Construct the board
    current_board = game.Board(players)

    # Start the game
    current_board.start_game()
    print(current_board.history_cards)
    print("The game has ended.\n")

    mySymbol = card.Symbol("♠")
    print(mySymbol)
    print(mySymbol.__doc__)

    myCard = card.Card(12, "♠")
    print(myCard)
    print("\n\n\n\n")
    # print(len(current_board.active_cards))
#    card.Card.print_cards(current_board.active_cards)

    print(card.Symbol("♠"))
    print(card.Card(5, "♠"))
    print(card.Card.list_card_names([myCard, myCard]))
    print(card.Symbol.__doc__)
    print(card.Card.__doc__)
    print("\n\n")
    print(card.Symbol.assign_color.__doc__)
    print("\n\n")
    print(card.Card.list_card_names.__doc__)
    myPlayer = player.Player("Ece")
    print(myPlayer)
