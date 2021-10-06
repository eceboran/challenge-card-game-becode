from utils import player
from utils import game

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("The game will start")

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
    print("The game has ended.")
