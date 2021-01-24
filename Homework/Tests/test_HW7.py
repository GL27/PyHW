from ..HW7 import *


def test_flip_phone1():
    expected = '4433555555666110966677755531111'
    actual = flip_phone('Hello, World!')
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'


def test_flip_phone2():
    expected = '777783388833'
    actual = flip_phone('Steve')
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'


def test_flip_phone3():
    expected = ''
    actual = flip_phone('')
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'


def test_unique_characters1():
    expected = 1
    actual = unique_characters('zzz')
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'


def test_unique_characters2():
    expected = 11
    actual = unique_characters('Coding is cool!')
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'


def test_unique_characters3():
    expected = 0
    actual = unique_characters('')
    assert actual == expected, f'Expected: {expected}, Actual: {actual}'


def test_car1():
    car = Car('Kia', 120, 60)
    car.accelerate()
    assert car.current_speed == 70, f'Expected: 65, Actual: {car.current_speed}'


def test_car2():
    car = Car('Chevy', 100, 95)
    car.accelerate()
    assert car.current_speed == 95, f'Expected: 95, Actual: {car.current_speed}'


def test_car3():
    car = Car('Lamborghini', 300, 5)
    car.decelerate()
    assert car.current_speed == 5, f'Expected: 5, Actual: {car.current_speed}'
