import pytest

from program import *


def test_player_name() -> None:
    """
    Tests the if the player's name has been initialized correctly, and
    the get_name() function return's the player's name
    """
    p1 = Player("Bob")
    assert p1.get_name() == "Bob"


def test_ship_set_destroyed() -> None:
    """
    Tests if the ship is correctly initialized not destroyed, and gets
    correctly destroyed after calling get_destroyed()
    """

    s = Ship(0, 0)
    assert not s.get_destroyed()
    s.set_destroyed()
    assert s.get_destroyed()


def test_setup_ships() -> None:
    """
    Tests if the player is able to setup ships using a list
    of coordinates through the setup_ships() method
    """
    coordinates = [[2, 3], [4, 4], [1, 2], [1, 3]]
    p1 = Player("Bob")
    assert p1.get_ships() == []
    p1.setup_ships(coordinates)
    assert p1.get_ships() == coordinates


def test_check_turn() -> None:
    """
    Tests if the correct players turn is being returned,
    through the check_turn() function
    """
    player_1 = Player("Bob")
    player_2 = Player("Steve")
    turn_number = 2
    assert check_turn(player_1, player_2, turn_number) == "Steve"

def test_setup() -> None:
    player_1 = Player(input("Bob"))
    player_2 = Player(input("Joe"))

    assert True

if __name__ == '__main__':
    pytest.main(['Code Night #7/Battleship/unit_testing.py'])