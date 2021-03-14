from typing import List


class Board:
    
    __tiles: List[List[str]]

    def __init__(self):
        """
        Initialize a 5x5 grid using nested lists, where each element (tile)
        is represented with an "E" for empty.
        """

        self.__tiles = [["E", "E", "E", "E", "E"],
                        ["E", "E", "E", "E", "E"],
                        ["E", "E", "E", "E", "E"],
                        ["E", "E", "E", "E", "E"],
                        ["E", "E", "E", "E", "E"]]

    def get_tile(self, x, y):
        return self.__tiles[x][y]

    def set_tile(self, x, y, value):
        """
        Changes the tile at the specific x, y coordinates

        """
        self.__tiles[x][y]

    def print_board(self, with_alive_ships):
        """
        Print the entire board in a 5x5 grid, each tile separated with "\t".
        Use the following convention:
        "O" - miss
        "X" - a hit ship
        "." - empty

        Display un-hit, alive ships with an "S" if and only if with_alive_ships is True,
        otherwise, display "."
        """
        for row in self.__tiles:
            row_output = ""
            for tile in row:
                row_output += tile + "\t"
            print(row_output)


class Ship:

    __location: List[int]
    __destroyed: bool

    def __init__(self, x, y):
        """
        """
        self.__location = [x, y]
        self.__destroyed = False

    def get_location(self):
        return self.__location

    def get_destroyed(self):
        return self.__destroyed

    def set_destroyed(self):
        self.__destroyed = True


class Player:

    __name: str
    __ships: List[Ship]
    __player_board: Board

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_player_board(self):
        return self.__player_board

    def setup_ships(self, coordinates):
        """
        Takes a list of sublist of coordinates, where the first element
        in each sublist is an x-coordinate, and the second element is
        a y-coordinate.

        Check if ship already exists at that location.
        Check if location is outside of the board.
        If the location is valid, then set create a new Ship.
        """
        ship_coords = []
        for coords in coordinates:
            x_coord, y_coord = coords[0], coords[1]
            if [x_coord, y_coord] in ship_coords:
                print("There's already a ship at that location")
                continue
            elif (x_coord or y_coord) > 4 or (x_coord or y_coord) < 0:
                print("These coordinates are outside of the board")
                continue
            new_ship = Ship(x_coord, y_coord)
            ship_coords.append([x_coord, y_coord])
            self.__ships.append(new_ship)

    def get_ships(self):
        return self.__ships

    
def check_turn(player_1, player_2, turn_number):
    """
    Return a string of the name of the player who's turn it is currently,
    based on the current turn_number. Player 1 always starts on turn #1.
    """
    if turn_number % 2 == 1:
        return player_1.get_name()
    else:
        return player_2.get_name()


# def define_ship_location():
#     pass


def setup():

    player_1 = Player(input("Type a name for player 1: "))
    player_2 = Player(input("Type a name for player 2: "))

    print(player_1.get_name(),"enter 4 ships you would like to setup")

    for i in range(2):
        ships = []
        for j in range(4):
            s = input("Enter the x and y coordinates of the ship you would like to enter separated by a comma (like this: x,y): ")
            x = s.split(",")[0]
            y = s.split(",")[1]
            ships.append([x, y])

        if i == 0:
            player_1.setup_ships(ships)
        elif i == 1:
            player_2.setup_ships(ships)


    """
    Allow the user to input 3 ships (using text input)
    Return two objects, player 1 and player 2 respectively, with their ships initialized
    """
    return player_1, player_2


def check_hit(board, x, y):


    pass


def check_win(player_1, player_2):
    # since ship is only one unit?
    if check_hit(player_1):
        return player_1.get_name()
    elif check_hit(player_2):
        return player_2.get_name()
    """
    Return the string of the name of the player if they have won.
    A player has won if and only if their opponent has ALL their ships destroyed.
    If nobody has won yet, return an empty string.
    """

    win = True

    for ship in player_1.get_ships():
        if not ship.get_destroyed():
            win = False

    if win:
        return player_2.get_name()

    win = True

    for ship in player_2.get_ships():
        if not ship.get_destroyed():
            win = False

    if win:
        return player_1.get_name()

    return ""


def save_game(player_1, player_2):
    """
    Save the current state of the game in two files called player_1.txt and player_2.txt,
    where each file stores the current state of player 1 and player 2's board respectively.

    Each row of the board should be on a separate line, where each tile is separated by a "\t".

    Each tile should be represented with the following:
    "D" - Destroyed ship
    "A" - Alive ship
    "M" - Missed tile
    "E" - Empty tile
    """
    f = open("player_1.txt", "w")
    board = player_1.get_player_board()
    f.write()


def load_game():
    """
    Load the game from two files called player_1.txt and player_2.txt,
    where each file stores the last saved state of player 1 and player 2's board respectively.

    Each row of the board is saved on a separate line, where each tile is separated by a "\t".

    Each tile should be represented with the following:
    "D" - Destroyed ship
    "A" - Alive ship
    "M" - Missed tile
    "E" - Empty tile
    """
    pass


"""
DO NOT TOUCH BELOW THIS LINE
"""

# if __name__ == '__main__':
#
#     play_again = "Y"
#
#     while play_again == "Y":
#         play_again = input("Would you like to play again? (Y/N): ")