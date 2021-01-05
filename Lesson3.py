# lists

arr = [1, 2, 3, True, 3.14, "pie"]

# print(arr[3])  # index
# print(arr[-2])

# print(arr[-4:-2])  # slicing


# print(arr[0:5:2])  # step
#
# print(arr[-5:-1:3])

print(arr[::-1])  # remember this

arr.append(5)
print(arr)

print(len(arr))  # length
arr[len(arr) - 1]   # alternate way to access last element