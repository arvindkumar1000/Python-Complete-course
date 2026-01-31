class Car:
    total_car =0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1

    def get_brand(self):
        return self.__brand + " !"
    
    # def get_model(self):
    #     return self.__model + " access by get method "

    @property
    def model(self):
        return self.__model

    def fullName(self):
        return f"{self.__brand} {self.__model}" 

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_Description():
        return "Cars are means of transport !"


class ElectricCar(Car):
    def __init__(self,brand,model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"   
     

my_tesla = ElectricCar("Tesla","Model S","85kWh")                

# print(my_tesla.fuel_type())SS

# print(safari.fuel_type())


My_safari_car = Car("Tata", "Safari")
# My_safari_car.model ="City"
test = Car("Tata","Nexon")

print(My_safari_car.model)
# print(Car.total_car)

# print(My_safari_car.general_Description())
# print(Car.general_Description())

# print(my_tesla.__brand)
# print(my_tesla.fullName())
# print(my_tesla.battery_size)
# print(my_tesla.get_brand())
# print(my_tesla.get_model())
# print(my_tesla.__model) ## don't access directly.  ( AttributeError) 