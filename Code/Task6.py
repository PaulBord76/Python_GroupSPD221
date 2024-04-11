"""
Даны 2 списка l1 = ['5', '10', 'Py', 'py'] и l2 = ['510', 'Python', 'Hello']
Определить все элементы списка l1, которые являются подстрокой элементов в l2
"""

l1 = ['5', '10', 'Py', 'py']
l2 = ['510', 'Python', 'Hello']

# p1, p2 = 0, 0
# res = []
#
# while p1 < len(l1):
#     while p2 < len(l2) - 1:
#         if l1[p1] in l2[p2] and l1[p1] not in res:
#             res.append(l1[p1])
#         p2 += 1
#     p1 += 1
#     p2 = 0
#
# print(res)

# all() and any()

# print(all([1, 1, 0])) # -> False
# print(all([1, 1, 1])) # -> True
# print(any([0, 0, 0])) # -> False

# res = [i for i in l1 if any(i in j for j in l2)]
# print(res)


