import sys

d1 = {}
d2 = dict()

# print(sys.getsizeof(d1))


# Через dict()
d3 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": "string",
    "e": [1, 2, 3],
    "g": {"aa": 11, "bb": 22}
}
d4 = dict(
    a=1,
    b=2,
    c=3
)
# print(d3)
# print(d4)

# Через список кортежей и zip()
l = [("a", 1), ("b", 2), ("c", 3)]
d5 = dict(l)
# print(d5)

l1 = [str(i) for i in range(10)]
l2 = [j**2 for j in range(10)]

print(l1)
print(l2)
print(dict(zip(l1, l2)))

# str1 = "aaaaa"
# str2 = "aabaa"
# print(list(zip(str1, str2)))


# Через fromkeys()
d6 = dict.fromkeys(["a", "b", "c"], 115)
d7 = dict.fromkeys("hello", 115)
print(d7)


# Через dict comprehension
d8 = {i: j**2 for i, j in enumerate(range(10))}
print(d8)

# Все ключи должны быть уникальными
names = {
    "name": "Batman",
    "name": "Robin"
}
print(names)


dct = {
    1: "int",
    1.0: "float",
    "True": "bool"
}
# print(dct)

dct1 = {
    ("a", "b"): 1
}

print(dct1)