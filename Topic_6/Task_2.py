class Soda:
    def __init__(self, topping):
        self.topping = topping

    def show_my_drink(self):
        if self.topping:
            print(f"Soda with {self.topping}")
        else:
            print("Soda with gas")


soda1 = Soda("lemon")
soda1.show_my_drink()

soda2 = Soda(None)
soda2.show_my_drink()