from grid import grid_to_string
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from player import Player

def test_grid1():
    board=[[Wall(),Wall(),Start(),Wall(),Wall()],[Wall(),Air(),Air(),Air(),Wall()],[Wall(),Wall(),End(),Wall(),Wall()]]
    expected=('''A*X**
*   *
**Y**\n
You have 0 water buckets.\n''')
    actual=grid_to_string(board,Player())
    assert expected == actual,'Grid simple board positive test failed.'
    print('Grid simple board positive test passed.')

def test_grid2():
    board = [[Wall(),Wall(),Start(),Wall(),Wall()],[Wall(),Teleport('2'),Air(),Water(),Wall()],[Wall(),Teleport('2'),Air(),Fire(),Wall()],[Wall(),Wall(),End(),Wall(),Wall()]]
    expected =('''A*X**
*2 W*
*2 F*
**Y**\n
You have 0 water buckets.\n''')
    actual = grid_to_string(board,Player())
    assert expected == actual,'Grid complex board positive test failed.'
    print('Grid complex board positive test passed.')

#There is no negative test case for grid since game_parser catch all of the negative test case

#Edge case
def test_grid4():
    board=[[Wall(),Wall(),Start(),Wall(),Wall()],[Wall(),Teleport('2'),Air(),Water(),Wall()],[Wall(),Teleport('2'),Air(),Fire(),Wall()],[Wall(),Wall(),End(),Wall(),Wall()]]
    expected= TypeError("grid_to_string() missing 1 required positional argument: 'player'")
    fail_message=('Grid edge case : invalid type mishandled :(')
    try:
        actual=grid_to_string(board)
    except TypeError as e:
        assert str(expected) == str(e), fail_message
        print("Grid edge case: invalid type handled correctly!")
    except Exception:
        print(fail_message)

def run_tests():
    test_grid1()
    test_grid2()
    test_grid3()
    test_grid4()
