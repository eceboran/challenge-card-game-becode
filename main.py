# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils import card
from utils import player
from utils import deck
from utils import game
from random import shuffle, choice




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")



myCard = card.Card("red",'a','n')

print(myCard.__dict__)

myPlayer = player.Player('Ece')

print(myPlayer.__dict__)

help(shuffle)
help(choice)

myDeck = deck.Deck()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
