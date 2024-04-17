def increase_g(g):
    return g() + 1

def g():
    return 1

result = increase_g(g)
print(result)
