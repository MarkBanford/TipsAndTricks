# Define a class attribute”colour” with a default value white. I.e., Every Vehicle should be white.


class Vehicle:
    colour = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.colour, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
