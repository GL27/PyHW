from ..HW2 import *


def test_calculate_tax1():
    assert calculate_tax(5.50) == 5.99, f'Expected: 5.99, Actual: {calculate_tax(5.50)}'


def test_calculate_tax2():
    assert calculate_tax(11.99) == 13.05, f'Expected: 13.05, Actual: {calculate_tax(11.99)}'


def test_calculate_tax3():
    assert calculate_tax(205.56) == 223.8, f'Expected: 223.8, Actual: {calculate_tax(205.56)}'


def test_compute_hypotenuse1():
    assert compute_hypotenuse(3, 4) == 5, f'Expected: 5, Actual: {compute_hypotenuse(3, 4)}'


def test_compute_hypotenuse2():
    assert compute_hypotenuse(5, 12) == 13, f'Expected: 13, Actual: {compute_hypotenuse(5, 12)}'


def test_compute_hypotenuse3():
    assert compute_hypotenuse(36, 77) == 85, f'Expected: 85, Actual: {compute_hypotenuse(36, 77)}'


def test_distance1():
    assert distance(0, 0, 5, 5) == 50 ** 0.5, f'Expected: {50 ** 0.5}, Actual: {distance(0, 0, 5, 5)}'


def test_distance2():
    assert distance(4, 10, 7, 6) == 5, f'Expected: 5, Actual: {distance(4, 10, 7, 6)}'


def test_distance3():
    assert distance(-8, 10, 4, -5) == 369 ** 0.5, f'Expected: {369 ** 0.5}, Actual: {distance(-8, 10, 4, -5)}'


def test_is_leap_year1():
    assert is_leap_year(2000), f'Expected: True, Actual: False'


def test_is_leap_year2():
    assert is_leap_year(1400) == False, f'Expected: False, Actual: True'


def test_is_leap_year3():
    assert is_leap_year(2003) == False, f'Expected: False, Actual: True'


def test_is_leap_year4():
    assert is_leap_year(1992), f'Expected: True, Actual: False'
