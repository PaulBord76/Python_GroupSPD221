"""
Создать список из N элементов (числа), которые будут вводиться через  input().
Первым вводом нужно указать рамер списка.
Найти максимальное значение полученного списка.
"""

# n = int(input("N: "))
# res = []
# i = 0
#
# while i < n:
#     num = input("Number: ")
#     if num.isdigit():
#         res.append(num)
#     else:
#         print(f"{num} is not digit")
#     i += 1

# print(max(res))

print(max([int(input("Number: ")) for _ in range(int(input("N: ")))]))