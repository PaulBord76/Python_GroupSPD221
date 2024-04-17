lst = [1, 15, 35, 4, 1, 15]

def func(lst):
    unique_lst = []
    for el in lst:
        if el not in unique_lst:
            unique_lst.append(el)
    return unique_lst

print(func(lst))