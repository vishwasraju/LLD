#---------------------------bad practice: inheritance------------------------

class Car:
    def start_engine(self):
        print("Starting normal engine")


class ElectricCar(Car):
    def start_engine(self):
        print("Starting electric motor")


car = ElectricCar()
car.start_engine()

#Child changes parent's behaviour.
#Different engine types make inheritance complicated.
#__________________________________________________________________


#---------------------------good practice: composition------------------------

class Engine:
    def start(self):
        print("Engine started")


class ElectricMotor:
    def start(self):
        print("Electric motor started")


class Car:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain

    def start(self):
        self.drivetrain.start()


petrol_car = Car(Engine())
electric_car = Car(ElectricMotor())

petrol_car.start()
electric_car.start()

#Output:
#Engine started
#Electric motor started

#Car HAS-A drivetrain.
#Car delegates work to its drivetrain.
#We can change the drivetrain without modifying Car.
#Composition = HAS-A relationship.
#Inheritance = IS-A relationship.
#__________________________________________________________________