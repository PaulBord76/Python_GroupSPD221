m = int(input("Введите количество ингредиентов на складе "))

ingredient = {}

for i in range(1, m+1):
    print("Введите ингредиент на складе " )
    ingredient[input()] = i

n = int(input("Введите количество ингредиентов для рецепта "))

recipe = {}

for i in range(1, n+1):
    print("Введите ингредиент для рецепта " )
    recipe[input()] = i

print(ingredient)
print(recipe)

products = {}

for a in recipe:
    if a in ingredient:
        products[a] = "Присутствует"
    else:
        products[a] = "Отсутствует"

print(products)