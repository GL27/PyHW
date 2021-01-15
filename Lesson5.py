import random

l = [1, 2, 3, 4]

# for i in range(0, len(l)):
    # print(l[i])

def binary(num):
    num = num[::-1]
    sum = 0
    for i in range(0, len(num)):
        sum += (2 ** i) * int(num[i])
    return sum

# print(binary('10011'))

x = 5
if x > 0:
    print('x is positive')
elif x == 0: # else if
    print('x is 0')
elif x == 5:
    print('x is 5')
else:
    print('x is negative')


def weekend_or_weekday(num):
    if num <= 5:
        print('weekday')
    else:
        print('weekend')


# weekend_or_weekday(5)

# A: 90+, B: 80 <= x < 89, C: 70 <= x < 79, D: 60 <= x 69, F: < 60


def grades(num):
    if num >= 90:
        print('A')
    elif num >= 80:
        print('B')
    elif num >= 70:
        print('C')
    elif num >= 60:
        print('D')
    else:
        print('F')


# grades(55)


# break and continue
for x in range(0, 11):
    if x == 5:
        break  # breaks the loop
    # else:
        # print(x)


for x in range(1, 20):
    if x % 2 == 0:
        continue  # continues to next iteration
    # print(x)


def is_sorted(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogo_sort(arr):
    while True:
        if is_sorted(arr):
            break
        else:
            random.shuffle(arr)
    return arr

# print(bogo_sort([55, -20, -19, 5, 3, 2, 20, 35, -55, 12]))
print(sorted([55, -20, -19, 5, 3, 2, 20, 35, -55, 12]))