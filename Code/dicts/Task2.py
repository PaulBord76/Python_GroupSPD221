"""
Дана цепочка ДНК, первая нить которой состоит из следующих нуклеотидов:
AATCCTGGATTCTAC

Задача - достроить вторую цепочку используя принцип комплементарности:
А - Т
С - G
G - C
T - A
"""
dct = {
    "A": "T",
    "C": "G",
    "G": "C",
    "T": "A"
}

chain1 = "AATCCTGGATTCTAC"


# for i in chain1:
#     chain2 += dct[i]
#
# print(chain2)

chain2 = "".join([dct[i] for i in chain1])
print(chain2)