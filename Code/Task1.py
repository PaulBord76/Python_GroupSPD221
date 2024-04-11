"""
Есть список [1, 2, 3, 4, 4, 7, 6, 8, 10]. Вывести все четные элементы.
"""

lst = [1, 2, 3, 4, 4, 7, 6, 8, 10]

for i in lst:
    if i % 2 != 0:
        print(i)

res = [i for i in lst if i % 2 == 0]
print(res)