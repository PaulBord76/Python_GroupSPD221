dct = {
    "one": 1,
    "two": 2,
    "three": 3
}
dct1 = {
    "four": 4
}

# print(dct["one"])
dct["one"] = 2
# print(dct)
# print(dct["four"])

# print(dct.get("four", {}))


# UNION
d = dct | dct1
print(d)
dct.update(dct1)
print(dct)

d1 = {**dct, **dct1}
print(d1)

# k = d.keys() | {'five', 'six'}
# print(k)
# v = d.values() | {5, 6} # TypeError
# print(v)


for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(f"{k} -> {v}")