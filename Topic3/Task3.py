s = "10951351"

obj = {}
obj1 = {}

for char in s:
    sum = 0
    for char1 in s:
        if char1 == char:
            sum = sum + 1
    obj[char] = sum

print(obj)

temp = obj.copy()

sorted_obj = sorted(obj.items(), key=lambda item: item[1], reverse=True)

from collections import OrderedDict

output = OrderedDict()
for k, v in sorted_obj:
    if k not in obj1:
        obj1[k] = v
        if len(obj1) == 3:
            break

print(obj1)
