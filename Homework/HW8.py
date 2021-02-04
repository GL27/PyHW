# Gaby

"""
Problem 1
Implement bogosort on a list of numbers using the random module. The main idea of this is to shuffle an array until
it is sorted in ascending order. You will be using 3 different functions:
bogosort(arr)
    -This is the main function for sorting. It runs the loop and returns the sorted array.
is_sorted(arr):
    -This returns True if it is sorted and False otherwise.
    -If there is only one element, return True.
shuffle(arr):
    -This is where you implement your own algorithm for shuffling. I want you to use the Fisher-Yates algorithm,
    which you can learn about here: https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    -You will be using random for this function only, in which you randomly generate numbers. Use randint to generate
    the numbers.
    -Return the new array after shuffling it.
You will be tested on all three functions.
"""

import random

def is_sorted(arr):
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def shuffle(arr):
    n = len(arr)
    for i in range(0, n):
        x = random.randint(0, n-1)
        arr[i], arr[x] = arr[x], arr[i]


def bogosort(arr):
    n = len(arr)
    while not is_sorted(arr):
        shuffle(arr)



"""
Problem 2
There are several formulas to approximate pi. I want you to return its approximation using a Machin-like formula, which
goes as follows: 
pi/4 = 4arctan(1/5) - arctan(1/239)
Use arctan from the math module. Its documentation is here: https://docs.python.org/3/library/math.html
"""

import math
def approx_pi():
    return None


"""
Problem 3
The datetime module is used for all things date and time-related. One of the things it can do is return the day of the 
week for a datetime object, and that is done using the weekday() method. A datetime object holds the data representing a 
specific date. Look up the documentation for this module to see how it works. I want you to make a function that returns
a boolean for whether the given datetime object is a weekday. For instance, passing in datetime.date(2021, 1, 31) should
return False since 1/31/2021 is a Sunday.
"""


def is_weekday(date_obj):
    return None

