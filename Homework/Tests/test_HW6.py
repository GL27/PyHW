from itertools import permutations
from ..HW6 import *

with open('./Homework/HW6.py', 'r') as f:
    data = f.read()

    def test_digit_sum_recursion():
        assert data.count('digit_sum') > 1, 'digit_sum not recursive'

    def test_hanoi_recursion():
        assert data.count('hanoi') > 1, 'hanoi not recursive'

    def test_subset_sum_recursion():
        assert data.count('subset_sum') > 1, 'subset_sum not recursive'

    def test_permute_recursion():
        assert data.count('permute') > 1, 'permute not recursive'

def test_digit_sum():
    errors = []

    if (s := digit_sum(0)) != 0:
        errors.append(f'Input: 0, Expected: 0, Actual {s}')
    if (s := digit_sum(1)) != 1:
        errors.append(f'Input: 1, Expected: 1, Actual {s}')
    if (s := digit_sum(123)) != 6:
        errors.append(f'Input: 123, Expected: 6, Actual {s}')
    if (s := digit_sum(8972345971240123894712309487120347091328750129345)) != 205:
        errors.append(f'Input: 8972345971240123894712309487120347091328750129345, Expected: 205, Actual {s}')
    if (s := digit_sum(-1)) != 1:
        errors.append(f'Input -1, Expected: 1, Actual {s}')
    if (s := digit_sum(-54321)) != 15:
        errors.append(f'Input: -54321, Expected: 15, Actual {s}')

    assert not errors, '\n'.join(errors)

def test_hanoi():
    errors = []

    for i in range(15):
        if (s := hanoi(i)) != 2**i - 1:
            errors.append(f'Input: {i}, Expected: {2**i - 1}, Actual: {s}')

    assert not errors, '\n'.join(errors)

def test_subset_sum():
    errors = []

    if not (b := subset_sum([], 0)):
        errors.append(f'Input: ([], 0), Expected: True, Actual: {b}')
    if b := subset_sum([], 1):
        errors.append(f'Input: ([], 1), Expected: False, Actual: {b}')
    if not (b := subset_sum([1, 2, 3], 0)):
        errors.append(f'Input: ([1, 2, 3], 0), Expected: True, Actual: {b}')
    if not (b := subset_sum([1], 1)):
        errors.append(f'Input: ([1], 1), Expected: True, Actual: {b}')
    if not (b := subset_sum([2, 1, -1, 5], 1)):
        errors.append(f'Input: ([2, 1, -1, 5], 1), Expected: True, Actual: {b}')
    if not (b := subset_sum([2, 1, -1, 5], 6)):
        errors.append(f'Input: ([2, 1, -1, 5], 6), Expected: True, Actual: {b}')
    if not (b := subset_sum([2, 1, 5, 17, 7, -13, -19, 11], 15)):
        errors.append(f'Input: ([2, 1, 5, 17, 7, -13, -19, 11], 15), Expected: True, Actual: {b}')
    if not (b := subset_sum([2, 1, 5, 17, 7, -13, -19, 11], -27)):
        errors.append(f'Input: ([2, 1, 5, 17, 7, -13, -19, 11], -27), Expected: True, Actual: {b}')
    if b := subset_sum([2, 1, 5, 17, 7, -13, -19, 11], 44):
        errors.append(f'Input: ([2, 1, 5, 17, 7, -13, -19, 11], 44), Expected: False, Actual: {b}')

    assert not errors, '\n'.join(errors)

def test_permute():
    errors = []
    lists = [[], [1, 2, 3], [3, 2, 1], ['a', 'b', 'c'], ['cat', 'dog', 'bird', 'fish', 'hamster', 'snake']]

    for array in lists:
        missing = []
        p = permute(array)
        for permutation in permutations(array):
            if p is None or list(permutation) not in p:
                missing.append(list(permutation))
        if missing:
            errors.append(f'Input: {array}, Missing permutations: {", ".join([str(m) for m in missing])}')

    assert not errors, '\n'.join(errors)
