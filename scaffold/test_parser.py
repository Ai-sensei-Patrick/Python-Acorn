from game_parser import parse
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

#positive test
def test_parse1():
    board=['**X**\n','*   *\n','**Y**']
    expected = True
    parsed=parse(board)
    for items in parsed:
        for i in items:
            if isinstance(i,Air) or isinstance(i,Wall) or isinstance(i,Start) or isinstance(i,End) :
                actual = True
    assert expected == actual,'Parse simple board positive test failed.'
    print('Parse simple board positive Test passed.')

def test_parse2():
    board=['**X**\n','**Y**']
    expected = True
    parsed=parse(board)
    for items in parsed:
        for i in items:
            if isinstance(i,Air) or isinstance(i,Start) or isinstance(i,End) :
                actual = True
    assert expected == actual,'Parse small board positive test failed.'
    print('Parse small board positive Test passed.')

def test_parse3():
    board=['**X***\n','* F 2 *\n','*  ** *\n','* W 2 *\n','***Y**']
    expected = True
    parsed=parse(board)
    for items in parsed:
        for i in items:
            if isinstance(i,Air) or isinstance(i,Wall) or isinstance(i,Start) or isinstance(i,End) or isinstance(i,Teleport) or isinstance(i,Water) or isinstance(i,Fire):
                actual = True
    assert expected == actual,'Parse complex board positive test failed.'
    print('Parse complex board positive test passed.')

#negative test
def test_parse4():
    board=['*****\n','*   *\n','**Y**']
    expected = ValueError('Expected 1 starting position, got 0.')
    fail_message = "Test no starting position: invalid type mishandled :("
    try:
        actual = parse(board)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test no starting position: invalid type handled correctly!")
    except Exception:
        print(fail_message)


def test_parse5():
    board=['**X**\n','*   *\n','*****']
    expected = ValueError('Expected 1 ending position, got 0.')
    fail_message = "Test no ending position: invalid type mishandled :("
    try:
        actual = parse(board)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test no ending position: invalid type handled correctly!")
    except Exception:
        print(fail_message)

def test_parse6():
    board=['**X**\n','*  2*\n','**Y**']
    expected = ValueError('Teleport pad 2 does not have an exclusively matching pad.')
    fail_message = "Test teleport pad does not have matching pad: invalid type mishandled :("
    try:
        actual = parse(board)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test teleport pad does not have matching pad: invalid type handled correctly!")
    except Exception:
        print(fail_message)

def test_parse7():
    board=['**X**\n','*  B*\n','**Y**']
    expected = ValueError('Bad letter in configuration file: B.')
    fail_message = "Test bad letter in configuration: invalid type mishandled :("
    try:
        actual = parse(board)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test bad letter in configuration: invalid type handled correctly!")
    except Exception:
        print(fail_message)
#edge case
def test_parse8():
    board=[]
    expected = ValueError('Expected 1 starting position, got 0.')
    fail_message='Edge test for parse Failed.'
    try:
        actual = parse(board)
    except ValueError as e:
        assert str(e) == str(expected), fail_message
        print('Edge test for parse passed.')
    except Exception:
        print(fail_message)


def run_tests():
    test_parse1()
    test_parse2()
    test_parse3()
    test_parse4()
    test_parse5()
    test_parse6()
    test_parse7()
    test_parse8()
