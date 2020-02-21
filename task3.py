class Car():
    def __init__(self,mark,model,year):
        self.mark = mark
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70
    
    def __add_distance(self, km):
        self.odometer += km
    
    def __subtract_fuel(self, km):
        self.fuel -= km/10
    
    def drive(self, km):
        if (self.fuel - km/10) >= 0:
            self.__add_distance(km)
            self.__subtract_fuel(km)
            print("Lets Drive!!!")
        else:
            print("Need more Fuel, Fill up")

car1 = Car("Honda", "Fit", "2020")
print(car1.mark,car1.model,car1.year)
car1.drive(100)
print(car1.odometer)
print(car1.fuel)
