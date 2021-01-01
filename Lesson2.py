def multiply(a, b):
    return a * b

num1 = 5
num2 = 3
print(multiply(num1, num2))

# scope
print(num1)
# print(a) outside of scope


# f-strings
def make_greeting(name):
    return f'Hello {name}'

print(make_greeting('Steve'))