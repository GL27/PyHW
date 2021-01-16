# Gaby

"""
Problem 1
Given the three side lengths of a triangle, return as a string whether it is equilateral, isosceles, or scalene.
"""


def triangle_type(a, b, c):
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'



"""
Problem 2
A Caesar Cipher is a very old way to encrypt a message. It takes every letter of a message and shifts it to the left
or right a certain number of times. For example, 'Dad' shifted 3 times to the right would be 'Gdg'.
Your job is to implement this cipher and return the encrypted message as a string. 
You should definitely use ASCII to complete this, which is a table of numbers corresponding to single characters. 
On this chart, 65 is 'A', 66 is 'B', and so on. 97 is 'a', and 98 is 'b'. Using this table will make shifting the 
letters so much easier. 
Python has two functions that will be useful for this:
    - ord() takes in a character and gives its ASCII code, so ord('a') will return 97. 
    - For doing the opposite, chr() takes in an int and returns the corresponding character. For instance, chr(97) 
    returns 'a'. 
It might also help to use .islower() and .isupper(), which return whether a string is lowercase. For instance,
'c'.islower() returns True. There are multiple ways to solve this, so they might not be necessary.
Keep in mind that a Caesar Cipher only affects letters, so keep everything else, such as punctuation and whitespace, 
the same. 
Note: To make this somewhat easier, the shift will only be positive numbers, so you will go through the alphabet
from A to Z and back around to A.
The table: http://www.asciitable.com/
"""


def caesar_cipher(message, shift):
    return None


"""
Problem 3
Given a letter as a string, return a string saying whether it is a 'vowel' or 'consonant'. For 'y', return 'sometimes'.
"""


def is_vowel(letter):
    if letter in ('a', 'e', 'i', 'o', 'u'):
        return 'Vowel'
    elif letter in 'y':
        return 'Sometimes'
    else:
        return 'Consonant'


"""
Problem 4
Implement a function that turns a word into Pig Latin. There are two rules:
    -If a word begins with a consonant, including 'y', remove all the consonants up until the first vowel, place them
    at the end of the word, and then add 'ay' to the end of the word. Examples: 'computer' becomes 'omputercay' and 
    'think' becomes 'inkthay'.
    -If the word begins with a vowel, not including 'y', add 'way' to the end of the word. For example, 'algorithm'
    becomes 'algorithmway' and 'office' becomes 'officeway'.
"""


def pig_latin(word):
    return None
