"""
Есть список [1, 1, 2, 3, 3, 4, 5, 5, 5].
Убрать дублирующие элементы.
"""

lst = [1, 1, 2, 3, 3, 4, 5, 5, 5]
# res = []
#
# for i in lst:
#     if i not in res:
#         res.append(i)
# print(res)

p1, p2 = 0, 0

while p1 < len(lst):
    while p2 < len(lst) - 1 and lst[p2] == lst[p2 + 1]:
        p2 += 1

    lst[p1] = lst[p2]
    p1 += 1
    p2 += 1

    if p2 == len(lst):
        print(lst[:p1])
        break

# print(lst[:p1])




