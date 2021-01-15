from ..HW5 import *


def test_triangle_type1():
    assert triangle_type(3, 3, 3).lower() == 'equilateral', f"Expected: 'equilateral', Actual: {triangle_type(3, 3, 3).lower()}"


def test_triangle_type2():
    assert triangle_type(5, 4, 4).lower() == 'isosceles', f"Expected: 'isosceles', Actual: {triangle_type(5, 4, 4).lower()}"


def test_triangle_type3():
    assert triangle_type(5, 4, 4).lower() == 'isosceles', f"Expected: 'isosceles', Actual: {triangle_type(5, 4, 4).lower()}"


def test_caesar_cipher1():
    actual = caesar_cipher('Hello!', 3)
    assert actual == 'Khoor!', f"Expected: 'Khoor!', Actual: {actual}"


def test_caesar_cipher2():
    actual = caesar_cipher("Excuse me, why isn't my code working?", 6)
    assert actual == "Kdiayk sk, cne oyt'z se iujk cuxqotm?", f"Expected: \'Kdiayk sk, cne oyt\'z se iujk cuxqotm?\', Actual: {actual}"


def test_caesar_cipher3():
    actual = caesar_cipher("steve", 12)
    assert actual == "efqhq", f"Expected: 'efqhq', Actual: {actual}"


def test_is_vowel1():
    assert is_vowel('a').lower() == 'vowel', f"Expected: 'vowel', Actual: {is_vowel('a').lower()}"


def test_is_vowel2():
    assert is_vowel('w').lower() == 'consonant', f"Expected: 'consonant', Actual: {is_vowel('w').lower()}"


def test_is_vowel3():
    assert is_vowel('y').lower() == 'sometimes', f"Expected: 'sometimes', Actual: {is_vowel('y').lower()}"


def test_pig_latin1():
    assert pig_latin('computer') == 'omputercay', f"Expected: 'omputercay', Actual: {pig_latin('computer')}"


def test_pig_latin2():
    assert pig_latin('steve') == 'evestay', f"Expected: 'evestay', Actual: {pig_latin('steve')}"


def test_pig_latin3():
    assert pig_latin('apple') == 'appleway', f"Expected: 'appleway', Actual: {pig_latin('apple')}"
