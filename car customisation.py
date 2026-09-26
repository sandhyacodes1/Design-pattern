
class Car:
    def cost(self):
        return 25000

    def description(self):
        return "Car"

# ==========================================
# 2. BASE DECORATOR 
# ==========================================
class CarDecorator:
    def __init__ (self, car):
        self.car = car

    def cost(self):
        return self.car.cost()

# ==========================================
# 3. CONCRETE DECORATORS 
# ==========================================
class gpsDecorator(CarDecorator):

    def cost(self):
        return self.car.cost() + 500

class sunroofDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1000

class leatherDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1500
class sounddecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 800

# ==========================================
# 4. CLIENT - CREATE CAR 
# ==========================================


car = Car()
car = gpsDecorator(car)
car = sunroofDecorator(car)
car = leatherDecorator(car)
car = sounddecorator(car)


print(car.cost())
