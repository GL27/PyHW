# Dictionaries

dict = {
    'name': 'steve', # hashable keys
    'ok': 'boomer',
    'what are': 'those'
}

print(dict['ok']) # access values

print(dict.get('ok')) # also access values
print(list(dict.keys()))
print(dict.values())
print(dict.items())
dict.update({True: True})
print(dict.items())
dict[5] = True # 5 is not an index
print(dict)
dict.popitem() # removes most recent pair
print(dict)

del dict['ok']
print(dict)
# dict.clear() # empties dictionary
# print(dict)

for key in dict:
    print(dict[key])


# Classes

class Employee:
    raise_amount = 1.13 # class variable

    def __init__(self, first, last, pay): # double-underscore function "dunder"
        self.first = first # attribute
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@email.com'

    def full_name(self): # a method
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay *= self.raise_amount


ken = Employee('Ken', 'Yuen', 1200)
gab = Employee('Gaby', 'Lin', 2000000)

print(ken.email)
print(gab.email)
gab.email = 'w@w.com'
print(gab.email)
print(ken.full_name())
print(ken.raise_amount)
print(gab.raise_amount)
ken.apply_raise()
print(ken.pay)
gab.apply_raise()
print(gab.pay)
