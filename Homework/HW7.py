# YOUR NAME HERE

"""
Problem 1
Pretend you have a flip phone that uses multiple button presses to get a character.
Here's a table mapping the button to the characters:
Key   Character
1     .,?!:
2     ABC
3     DEF
4     GHI
5     JKL
6     MNO
7     PQRS
8     TUV
9     WXYZ
0     Space
For instance, pressing 4 twice gets 'H'.
Implement the function to use a dictionary to turn a string into a string of button presses. 'Hello, World!' becomes
4433555555666110966677755531111. Account for both uppercase and lowercase letters. The button's don't differentiate
for capitalization, you can adjust the input for the table. You can ignore every other that's not shown in the table.
"""


def flip_phone(message):
    message = message.lower()
    dict = {
        '1': '.,?!:',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '
    }
    result = ''
    for character in message:
        for x, y in dict.items():
            character = int()
            if character in range(y.index(character)) + 1:
                result += x
    return result


"""
Problem 2
Use one or more dictionaries to see how many unique characters are in a string.
For instance, 'zzz' has one unique character while 'Hello, World!' has 10. 
"""


def unique_characters(string):
    characters = {}
    for x in string:
        characters[x] = True
    return len(characters)


"""
Problem 3
Create a Car class with the attributes brand, max_speed, and current_speed. Initialize all those attributes in its
constructor in that order. Add two methods, accelerate and decelerate, which take no parameters, 
and add 10 to current_speed in accelerate and subtract 5 in decelerate. Check if accelerating will go past max_speed 
and if decelerating will make it go past 0. If either situation happens, don't change the speed.
"""

class Car:

    def __init__(self, brand, max_speed, current_speed):
        self.brand = brand
        self.max_speed = max_speed
        self.current_speed = current_speed

    def accelerate(self):
        if self.current_speed + 10 > self.max_speed:
             self.current_speed
        else:
            self.current_speed += 10

    def decelerate(self):
        if self.current_speed - 5 <= 0:
            self.current_speed
        else:
            self.current_speed -= 5