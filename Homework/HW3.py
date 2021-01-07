# YOUR NAME HERE

"""
Problem 1
Return the range of a list of ints. Assume that it is sorted.
"""


def list_range(arr):
    return arr[-1] - arr[0]


"""
Problem 2
Switch the elements of a list at index a and b and return the new list. Assume that every list will have at least two 
elements. 
"""


def switch(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


"""
Problem 3
Return the Chinese zodiac as a string corresponding to the year given as an int. For testing purposes, use 
rat, ox, tiger, rabbit, dragon, snake, horse, sheep, monkey, rooster, dog, pig. 
"""


def zodiac(year):
    signs = ['monkey', 'ox', 'tiger', 'rabbit', 'rat', 'snake', 'dog', 'sheep', 'dragon', 'rooster', 'horse', 'pig']
    return signs[year % 12]



"""
Problem 4
In one line of code, return every 7th number starting from the last element going backwards using indices and slicing. 
You should only need to modify the return statement to do this. The result should be 777, 770, ... all the way to 0. 
"""


def seventh_number():
    arr = list(range(0, 778))
    return arr[::-7]


