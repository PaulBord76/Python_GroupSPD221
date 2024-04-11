"""
Удалить все пары ключ-значение, значения которых начинаются с а (лат)
"""

dct = {
    "1": "apple",
    "2": "microsoft",
    "3": "atari",
    "4": "google"
}
print({k: v for k, v in dct.items() if not v.startswith("a")})

