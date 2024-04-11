dict1 = ["a", "b", "c", "d"]
dict2 = [1, 2, 3, 4]

obj = {}

k = 0

for char in dict1:

    obj[char] = dict2[k]
    k += 1

print(obj)

