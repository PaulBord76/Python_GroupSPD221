str = "pythonist"

obj = {}

for char in str:
    sum = 0

    for char1 in str:
        if char1 == char:
            sum = sum + 1
            v = sum
        else:
            v = 1

    obj[char] = v


print(obj)
