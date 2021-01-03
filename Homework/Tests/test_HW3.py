from ..HW3 import *


def test_list_range1():
    assert list_range([-5, 0, 5]) == 10, f'Expected: 10, Actual: {list_range([-5, 0, 5])}'


def test_list_range2():
    l = [-76, -74, -56, -54, -50, -46, -44, -35, -14, -11, -7, -1, 30, 44, 57, 62, 67, 74, 83, 89]
    assert list_range(l) == 165, f'Expected: 165, Actual: {list_range(l)}'


def test_list_range3():
    l = [-9907, -9537, -9412, -9316, -8746, -8587, -8449, -7783, -6802, -6759, -6112, -5740, -5515, -5447, -5165, -4703, -3941, -3297, -3140, -3060, -2956, -2133, -1501, -1034, -919, -745, -266
, 359, 433, 740, 1073, 1170, 1408, 1526, 3434, 3820, 4135, 4920, 5479, 5757, 5877, 5963, 6997, 7055, 8195, 8605, 9102, 9286, 9715, 9838]
    assert list_range(l) == 19745, f'Expected: 19745, Actual: {list_range(l)}'


def test_switch1():
    assert switch([1, 2], 0, 1) == [2, 1], f'Expected: [2, 1], Actual: {switch([1, 2], 0, 1)}'


def test_switch2():
    assert switch(['my', 'dear', 'aunt', 'sally'], 0, -1) == ['sally', 'dear', 'aunt', 'my'], f"Expected: {['sally', 'dear', 'aunt', 'my']}, {switch(['my', 'dear', 'aunt', 'sally'], 0, -1)}"


def test_switch3():
    l = [True, False, "3", 5]
    assert switch(l, 2, 1) == [True, "3", False, 5], f'Expected: {[True, "3", False, 5]}, Actual: {switch(l, 2, 1)}'


def test_zodiac1():
    assert zodiac(2002).lower() == 'horse', f'Expected: horse, Actual: {zodiac(2002).lower()}'


def test_zodiac2():
    assert zodiac(1776).lower() == 'monkey', f'Expected: monkey, Actual: {zodiac(1776).lower()}'


def test_zodiac3():
    assert zodiac(2020).lower() == 'rat', f'Expected: rat, Actual: {zodiac(2020).lower()}'


def test_seventh_number():
    l = []
    for x in range(0, 112):
        l.append(x * 7)

    assert seventh_number() == l[::-1], f'Expected: {l[::-1]}, Actual: {seventh_number()}'
