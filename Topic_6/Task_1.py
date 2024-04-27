class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, age):
        if type(age) == int and age >= 0:
            self.age = age
        else:
            print("Invalid age. Age shouldn't be a negative integer.")



user1 = User("Ben", 22)
print(user1.get_age())

user1.set_age(25)
print(user1.get_age())

user1.set_age(-20)
print(user1.get_age())
