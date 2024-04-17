def get_number_of_frogs(year: int) -> int:
    frogs = 120
    for i in range(1, year+1):
        frogs = 2*(frogs - 50)
    return frogs


print(get_number_of_frogs(3))
