# Card game simulator

## Description
This is the basis for a playing card game for the online casino `WeTakeYourMoney`.
When the game is run:
A deck of cards (52 cards) are created
The cards are split evenly between each player
At every turn, each player plays a single card, until there are no cards left.

## Installation
Download the repository from GitHub using:
```python
git@github.com:eceboran/challenge-card-game-becode.git`
```
The following libraries are required to run the program:
- typing
- random

## Usage
In the terminal, navigate to the folder that contains main.py.
To start the program, run:
```python
python main.py
```
Alternatively, you can open main.py in an IDE and run it there.

## Repository structure

### Main directory
Contains main.py which is the main program used to start the card game.
### Directory utils
Contains utility files for the card game.
- card.py: Contains the classes Symbol and Card
- player.py: Contains the class Player
- game.py: Contains the classes Board and Deck
 
## Timeline

| Day  | Completed tasks                                                |
| ---- | -------------------------------------------------------------- |
| 1    | Installed PyCharm 												|
|      | Set up the repository on GitHub                  				|
|      | Wrote the classes Symbol and Card                				|
| 2    | Completed writing the first working versions of the classes	|
|      | Ran the program with minor errors                      		|
| 3    | Improved the code and fixed minor errors        				|
|      | Ran the complete program successfully                          |
|      | Completed comments, typing the functions and docstrings       	|
|      | Completed the README file                     					|


## Personal situation
This project is my first challenge at [BeCode](https://becode.org/), following three weeks of learning basic and advanced Python concepts.


This project uses Black: The Uncompromising Code Formatter
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
