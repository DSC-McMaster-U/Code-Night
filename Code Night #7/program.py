from typing import List
class Board:
    
    __tiles: List[str]

    def __init__(self):
        """
        Initialize a 5x5 grid using nested lists, 
        """
        pass

    def get_tile(self, x, y):
        pass

    def set_tile(self, x, y):
        pass

class Ship:

    __location: List[int]
    __destroyed: bool

    def __init__(self):
        """
        """
        pass

    def get_location(self):
        pass

    def set_location(self, x, y):
        """
        
        """
        pass

    def get_destroyed(self):
        pass

    def set_destroyed(self):
        pass


class Player:

    __name: str
    __ships: List[Ship]
    __player_board: Board

    def __init__(self, name):
        pass

    def get_name(self):
        pass

    def get_player_board(self):
        pass

    def setup_ships(self):
        """
        Check if ship already exists at that location.
        Check if location is outside of the board.
        """
        pass

    
def check_turn(player_1, player_2, turn_number):
    """
    Return a string of the name of the player who's turn it is currently,
    based on the current turn_number. Player 1 always starts on turn #1.

    Pre-conditions:
    - turn_number >= 1
    """
    pass

def define_ship_location():
    pass

def setup():
    """
    Allow the user to input 3 ships
    """
    pass

def check_hit(board, x, y):
    pass

def check_win(player_1, player_2):
    """
    Return thestring of the name of the player if they have won.
    A player has won if and only if their opponent has all their ships destroyed.
    If nobody has won yet, return an empty string.
    """
    pass

def save_game(player_1, player_2):
    """
    Save the current state of the game in two files called player_1.txt and player_2.txt,
    where each file stores the current state of player 1 and player 2's board respectively.

    Each row of the board should be on a separate line, where each tile is separated by a "\t".

    Each tile should be represented with the following:
    "E" - Empty space
    "D" - Destroyed ship
    "A" - Alive ship
    """
    pass

def load_game():
    """
    """
    pass

"""
DO NOT TOUCH BELOW THIS LINE
"""

if __name__ == '__main__':

    play_again = "Y"
    
    while(play_again == "Y"):
        play_again = input("Would you like to play again? (Y/N): ")