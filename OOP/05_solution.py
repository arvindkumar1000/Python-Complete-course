class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand + " !"
    
    def get_model(self):
        return self.__model + " access by get method "

    def fullName(self):
        return f"{self.__brand} {self.__model}" 

    def fuel_type(self):
        return "Petrol or Diesel"



class ElectricCar(Car):
    def __init__(self,brand,model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"    

my_tesla = ElectricCar("Tesla","Model S","85kWh")                

print(my_tesla.fuel_type())



safari = Car("Tata", "Safari")
print(safari.fuel_type())

# print(my_tesla.__brand)
# print(my_tesla.fullName())
# print(my_tesla.battery_size)
# print(my_tesla.get_brand())
# print(my_tesla.get_model())
# print(my_tesla.__model) ## don't access directly.  ( AttributeError) 