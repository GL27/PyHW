import math
import random

from colored import fg, bg, attr

# import Lesson8b # module
# from Lesson8b import add, say_hello
# from Lesson8b import add as a, say_hello as hello
from Lesson8b import *

print(add(1, 2))
print(hungry())
print(say_hello())

# Python Standard Library
print(math.pi)
print(math.sin(math.pi))
print(math.cos(math.pi))
print(math.cos(0))
print(math.tan(math.pi / 4))
print(math.factorial(5))

print(random.randint(-10, 10))
arr = [1, 2, 3, 4, 5]
random.shuffle(arr)
print(arr)

print(random.choice([-5, 2, 33, 100]))

# Third-party libraries
print('%s Hello world! %s' % (fg(6), bg(169)))