def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

def euclid(n1, n2):
    if n1 % n2 == 0:
        return n2
    return euclid(n2, n1 % n2)

def add(i, j):
    if j == 0:
        return i
    #return add(i + 1, j - 1)
    return add(i ^ j, (i & j) << 1)

def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)

def collatz(n):
    if n == 1:
        return 0
    return 1 + collatz(n / 2 if n % 2 == 0 else 3 * n + 1)

def paren(n):
    if n == 0:
        return {''}
    parens = set()
    for i in range(n):
        for s in paren(n - i - 1):
            parens |= {'(' + p + ')' + s for p in paren(i)}
    return parens

def change(n):
    choices = {'P' * int(n / .01)}
    if n >= .25:
        choices |= {''.join(sorted('Q' + c)) for c in change(round(n - .5, 2))}
    if n >= .1:
        choices |= {''.join(sorted('D' + c)) for c in change(round(n - .1, 2))}
    if n >= .05:
        choices |= {''.join(sorted('N' + c)) for c in change(round(n - .05, 2))}
    return choices