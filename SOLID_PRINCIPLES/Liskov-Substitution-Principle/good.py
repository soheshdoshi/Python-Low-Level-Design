# "Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program


class Car:
    def __init__(self, type):
        self.type = type
        self.propties = {}
    def set_propties(self,color, gear, capacity):
        self.propties = {'color':color, 'gear': gear, 'capacity': capacity}
    def get_propties(self):
        return self.propties



class PetrolCar(Car):
    def __init__(self):
        super(PetrolCar, self).__init__(type)



car = Car("SUV")
car.set_propties("Red","Auto",6)

pt_car = PetrolCar("Sadan")
pt_car.propties("Blue", "Manual", 4)
