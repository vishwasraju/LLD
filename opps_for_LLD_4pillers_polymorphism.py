
#...............................................................
#---------------------------bad practice------------------------

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class ParkingLot:

    def park_vehicle(self, vehicle):

        if vehicle.vehicle_type == "CAR":
            print("Finding regular parking spot")

        elif vehicle.vehicle_type == "MOTORCYCLE":
            print("Finding small parking spot")

        elif vehicle.vehicle_type == "TRUCK":
            print("Finding large parking spot")


car = Vehicle("CAR")
bike = Vehicle("MOTORCYCLE")
truck = Vehicle("TRUCK")

parking = ParkingLot()

parking.park_vehicle(car)
parking.park_vehicle(bike)
parking.park_vehicle(truck)


#problem:
#ParkingLot directly checks every vehicle type.
#if we add Bus or Ambulance, we need to modify ParkingLot.
#this creates unnecessary dependencies.
#__________________________________________________________________


#---------------------------good practice--------------------------

from abc import ABC, abstractmethod
#common contract (abstraction)
class Vehicle(ABC):

    @abstractmethod
    def get_required_spot_size(self):
        pass
#Car implementation
class Car(Vehicle):

    def get_required_spot_size(self):
        return "REGULAR"

#Motorcycle implementation
class Motorcycle(Vehicle):

    def get_required_spot_size(self):
        return "SMALL"

#Truck implementation
class Truck(Vehicle):

    def get_required_spot_size(self):
        return "LARGE"

#ParkingLot depends on common behaviour, not specific vehicle types
class ParkingLot:

    def park_vehicle(self, vehicle):

        spot_size = vehicle.get_required_spot_size()

        print(f"Finding {spot_size} parking spot")


car = Car()
bike = Motorcycle()
truck = Truck()

parking = ParkingLot()

parking.park_vehicle(car)
parking.park_vehicle(bike)
parking.park_vehicle(truck)

#we can add Bus or Ambulance by creating new classes.
#no need to modify ParkingLot.
#all vehicles have the same method but different behaviour.
#this is called polymorphism.
#__________________________________________________________________
#...................................................................
