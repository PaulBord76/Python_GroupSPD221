from typing import List, Tuple

lst = [1, 2, 3, 4, 5, 6]

def get_pairs(lst: List) -> List[Tuple]:
    if len(lst) == 1:
        return None
    else:
        pairs = [(lst[i], lst[i+1]) for i in range(0, len(lst)-1, 2)]
        return pairs

print(get_pairs(lst))