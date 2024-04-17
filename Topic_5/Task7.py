def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


# Пример использования
a = 24
b = 36
print(gcd_recursive(a, b))  # Output: 12


def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Пример использования
a = 24
b = 36
print(gcd_iterative(a, b))  # Output: 12
