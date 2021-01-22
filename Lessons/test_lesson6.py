import math
from sys import argv

if argv[1] == 'factorial':
    from Lesson6 import factorial
    for i in range(100):
        assert (a := factorial(i)) == (e := math.factorial(i)), f'Input: {i}, Expected: {e}, Actual: {a}'

elif argv[1] == 'euclid':
    from Lesson6 import euclid
    for i in range(1, 100):
        for j in range(1, 100):
            assert (a := euclid(i, j)) == (e := math.gcd(i, j)), f'Input: ({i}, {j}), Expected: {e}, Actual: {a}'

elif argv[1] == 'add':
    from Lesson6 import add
    for i in range(100):
        for j in range(100):
            assert (a := add(i, j)) == i + j, f'Input: ({i}, {j}), Expected: {i + j}, Actual: {a}'

elif argv[1] == 'fib':
    from Lesson6 import fib
    fibs = [0, 1]
    def dynamic_fib(n):
        if n < len(fibs) - 1:
            return fibs[n]
        fibs.append(fibs[-1] + fibs[-2])
        return dynamic_fib(n)
    for i in range(30):
        assert (a := fib(i)) == (e := dynamic_fib(i)), f'Input: {i}, Expected: {e}, Actual: {a}'

elif argv[1] == 'collatz':
    from Lesson6 import collatz
    def collz(n):
        if n == 1:
            return 0
        return 1 + collz(n / 2 if n % 2 == 0 else 3 * n + 1)
    for i in range(1, 101):
        assert (a := collatz(i)) == (e := collz(i)), f'Input: {i}, Expected: {e}, Actual: {a}'

elif argv[1] == 'paren':
    from Lesson6 import paren
    def correct_paren(n):
        if n == 0:
            return {''}
        parens = set()
        for i in range(n):
            for s in correct_paren(n - i - 1):
                parens += {'(' + p + ')' + s for p in correct_paren(i)}
        return parens
    for i in range(13):
        assert len((a := paren(i)) - (e := paren(i))) == 0, f'Input: {i}, Expected: {e}, Actual: {a}'

elif argv[1] == 'change':
    from Lesson6 import change
    def correct_change(n):
        choices = {'P' * int(n / .01)}
        if n >= .25:
            choices |= {''.join(sorted('Q' + c)) for c in correct_change(round(n - .5, 2))}
        if n >= .1:
            choices |= {''.join(sorted('D' + c)) for c in correct_change(round(n - .1, 2))}
        if n >= .05:
            choices |= {''.join(sorted('N' + c)) for c in correct_change(round(n - .05, 2))}
        return choices
    for i in range(101):
        assert len((a := change(i / 100)) - (e := correct_change(i / 100))) == 0, f'Input: {i / 100}, Expected: {e}, Actual: {a}'

print('Correct')