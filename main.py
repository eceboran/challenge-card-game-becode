from utils import player
from utils import game

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("The game will start")

    # The player enters their name
    human_player_name = input("Please enter your name: ")
    # human_player_name = "Ece"
    # print(human_player_name)

    no_of_players = input("Please enter the total number of players: ")
    # no_of_players = '4'
    no_of_players = int(no_of_players)

    # Define the player names for the computer players
    player_names = [human_player_name]
    for new_player in range(no_of_players-1):
        player_names.append(f"Player {new_player+1}")

    # Create players
    players = []
    for player_name in player_names:
        print(player_name)
        if player_name == human_player_name:
            isHuman = True
        else:
            isHuman = False
        players.append(player.Player(player_name, isHuman))

    # Construct the board
    current_board = game.Board(players)
    # Start the game
    current_board.start_game()
    print("The game has ended.")
