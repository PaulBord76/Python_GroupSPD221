obj = {"One": "First", "Two": "Second", "Three": "Third", "Four": "Fourth", "Five": "Fifth"}

print(obj)

from collections import OrderedDict
dct = OrderedDict(obj)

print(dct)

first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)

print(dct)

second = list(dct.items())[1]
del dct[second[0]]

print(dct)

dct['new_key'] = 'new_value'

print(dct)
