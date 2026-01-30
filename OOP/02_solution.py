class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"    

MyCar = Car ("Toyota", "Corolla")
# print(MyCar.brand)
# print(MyCar.model)

print(MyCar.fullName())