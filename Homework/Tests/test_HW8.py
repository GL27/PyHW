from ..HW8 import *
import math
import datetime


def test_bogosort1():
    expected = [1, 2, 3]
    actual = bogosort([3, 2, 1])
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


def test_bogosort2():
    expected = [-23, 5, 12, 30]
    actual = bogosort([5, -23, 30, 12])
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


def test_bogosort3():
    expected = [1]
    actual = bogosort([1])
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


def test_is_sorted1():
    expected = False
    actual = is_sorted([3, 2, 1])
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


def test_is_sorted2():
    expected = True
    actual = is_sorted([-37, -36, -34, -14, -1, 2, 2, 18, 19, 34])
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


def test_is_sorted3():
    expected = True
    actual = is_sorted([2])
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


def test_shuffle():
    arr = [1, 2, 3, 4, 5]
    times = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }
    for x in range(10000):
        arr = shuffle(arr)
        times[arr[0]] += 1

    epsilon = 0.02
    is_distributed = True
    for value in times.values():
        if abs(1 / len(arr) - value / 10000) > epsilon:
            is_distributed = False

    assert is_distributed, f'Your shuffle is not evenly distributed'


def test_approx_pi():
    assert abs(approx_pi() - math.pi) <= 0.000000000000001, f'Your approximation of pi is not accurate'


def test_is_weekday1():
    day = datetime.date(2021, 1, 31)
    expected = False
    actual = is_weekday(day)
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


def test_is_weekday2():
    day = datetime.date(2002, 3, 22)
    expected = True
    actual = is_weekday(day)
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'


def test_is_weekday3():
    day = datetime.date(1776, 7, 4)
    expected = True
    actual = is_weekday(day)
    assert expected == actual, f'Expected: {expected}, Actual: {actual}'
