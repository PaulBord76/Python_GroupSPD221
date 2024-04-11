dct = dict(
    one=1,
    two=2,
    three=3
)

print(dct)

# del dct["three"]
# print(dct)

# POP, POPITEM

# i = dct.pop("two")
# print(i)
# print(dct)
#
#
# val = dct.popitem()
# print(val)
# print(dct)


# CLEAR

# dct.clear()
# print(dct)

# SET_DEFAULT
dct.setdefault("four")
print(dct)

# COPY

dct1 = dct.copy()
print(dct1)
dct["four"] = 4
print(dct)
print(dct1)
