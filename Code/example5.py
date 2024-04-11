from collections import Counter, OrderedDict


dct = dict(
    one=1,
    two=2,
    three=3
)
d = OrderedDict(dct)
print(type(d))


str_ = "python is awesome"
counter = Counter(str_)
print(OrderedDict(dict(counter)))
print(counter)
