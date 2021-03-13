import pytest

from program import Player
from program import Ship
from program import Board

def test_player_name() -> None:
    """
    Tests the if the player's name has been initialized correctly, and
    the get_name() function return's the player's name
    """
    p1 = Player("Bob")
    assert p1.get_name() == "Bob"

if __name__ == '__main__':
    pytest.main(['Code Night #7/unit_testing.py'])