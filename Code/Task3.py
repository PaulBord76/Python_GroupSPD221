"""
Есть список [10, 1, 9, 3, 6, 4, 7, 5, 8, 2, 0].
Отсортировать список любым способом
"""

lst = [10, 1, 9, 3, 6, 4, 7, 5, 8, 2, 0]
# lst.sort(key=lambda x: x % 2 != 0, reverse=True)
# l = sorted(lst)
# print(lst)


for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(lst)