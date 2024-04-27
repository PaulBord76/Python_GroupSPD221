class KgToPounds:
    def __init__(self, kg):
        self.kg = kg

    def get_kg(self):
        return self.kg

    def set_kg(self, new_kg):
        self.kg = new_kg

    def to_pounds(self):
        return self.kg * 2.20462


weight_converter = KgToPounds(10)
print(weight_converter.kg)
print(weight_converter.to_pounds())