from ..HW4 import *


def test_while_average1():
    assert while_average([5, 5, 5]) == 5, f'Expected: 5, Actual: {while_average([5, 5, 5])}'


def test_while_average2():
    assert while_average([-1, 5, 2, 1, -5]) == 0.4, f'Expected: 0.4, Actual: {while_average([-1, 5, 2, 1, -5])}'


def test_while_average3():
    assert while_average([-40, 9, -52, 43, -25, 94, -68, -78, -51, -87]) == -25.5, f'Expected: -25.5, Actual: {while_average([-40, 9, -52, 43, -25, 94, -68, -78, -51, -87])}'


def test_loop_average1():
    assert loop_average([5, 5, 5]) == 5, f'Expected: 5, Actual: {loop_average([5, 5, 5])}'


def test_loop_average2():
    assert loop_average([-1, 5, 2, 1, -5]) == 0.4, f'Expected: 0.4, Actual: {loop_average([-1, 5, 2, 1, -5])}'


def loop_while_average3():
    assert loop_average([-40, 9, -52, 43, -25, 94, -68, -78, -51, -87]) == -25.5, f'Expected: -25.5, Actual: {loop_average([-40, 9, -52, 43, -25, 94, -68, -78, -51, -87])}'


def test_palindromes1():
    assert palindromes(['racecar', 'bob', 'nice']) == 2, f"Expected: 2, Actual: {palindromes(['racecar', 'bob', 'nice'])}"


def test_palindromes2():
    assert palindromes(['my', 'dear', 'aunt', 'sally']) == 0, f"Expected: 0, Actual: {palindromes(['my', 'dear', 'aunt', 'sally'])}"


def test_palindromes3():
    assert palindromes(['steve', 'level', 'noon', 'anna']) == 3, f"Expected: 3, Actual: {palindromes(['steve', 'level', 'noon', 'anna'])}"


def test_max_1():
    assert max([1, 2, 3]) == 3, f'Expected: 3, Actual: {max([1, 2, 3])}'


def test_max_2():
    assert max([-8, 1, -1, 9, 4, -5, -4, 0, 2, 7]) == 9, f'Expected: 9, Actual: {max([-8, 1, -1, 9, 4, -5, -4, 0, 2, 7])}'


def test_max_3():
    assert max([926, -1645, 7045, 7922, -6963]) == 7922, f'Expected: 7922, Actual: {max([926, -1645, 7045, 7922, -6963])}'


def test_binary1():
    assert binary('10011') == 19, f"Expected: 19, Actual: {binary('10011')}"


def test_binary2():
    assert binary('1011010011') == 723, f"Expected: 723, Actual: {binary('1011010011')}"


def test_binary3():
    assert binary('100000000') == 256, f"Expected: 256, Actual: {binary('100000000')}"
