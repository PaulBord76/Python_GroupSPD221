"""
Дан список ['H', 'e', 'l', 'l', 'o']
Перевернуть список
"""

s = ['H', 'e', 'l', 'l', 'o']
# pointer = len(s) - 1
# new_s = []
#
# while pointer >= 0:
#     new_s.append(s[pointer])
#     pointer -= 1
#
# print(new_s)


p1 = 0
p2 = len(s) - 1

while p1 < p2:
    s[p1], s[p2] = s[p2], s[p1]
    p1 += 1
    p2 -= 1

print(s)



