''' Cohesion: Degree to which elements of function or class belong together. Strong Cohesion has clear responsibility
Coupling: How dependent how 2 parts of code are on each other
You want High Cohesion, but low coupling '''

import string
import random


class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percent = 0.05
        if self.electric:
            tax_percent = 0.02
        return tax_percent * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"ID: {self.id}")
        print(f"license_plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:
    vehicle_info = {}

    def add_vehicle_info(self, brand, electric, catalgue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalgue_price)  # key, values

    def __init__(self):
        self.add_vehicle_info("Tesla", True, 60_000)
        self.add_vehicle_info("VW", True, 35_000)
        self.add_vehicle_info("BMW", False, 45_000)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generarate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))} "

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)  # generate vehicle id of length 12
        license_plate = self.generarate_vehicle_license(vehicle_id)  # generate license plate
        return Vehicle(id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()  # create registry instance

        # Create a Vehicle
        vehicle = registry.create_vehicle(brand)

        # print vehicle reg info
        vehicle.print()


app = Application()
app.register_vehicle("VW")
