from interfaces import IDriver, IVehicle
from zope.interface import implementer
from zope.component import providedBy

@implementer(IDriver)
class Driver(object):
    """
    An implementation of IDriver interface.
    Implements a real driver.
    """
    def __init__(self, name, familyname):
        self.name=name
        self.familyname=familyname
        self.cars=[]
        self.motobikes=[]

    def fio(self):
        """
        Returns joint name and familyname
        """
        return "{} {}".format(self.name, self.familyname)

    def add_car(self, car):
        assert IVehicle.providedBy(car)
        self.cars.append(car)

    def remove_car(self, car):
        assert IVehicle.providedBy(car)
        self.cars.remove(car)
        
    def add_motobike(self, motobike):
        assert IVehicle.providedBy(motobike)
        self.motobikes.append(motobike)

    def remove_motobike(self, motobike):
        assert IVehicle.providedBy(motobike)
        self.motobikes.remove(motobike)

@implementer(IVehicle)
class Car(object):
    def __init__(self, name):
        self.name = name
        self.owner = self.number = None

    def register(self, owner, number):
        if self.owner is not None:
            raise ValueError("has owner")
        self.owner = owner
        self.number = number
        owner.add_car(self)

    def unregister(self):
        self.owner.remove_car(self)
        self.owner=None
        self.number=None
        
@implementer(IVehicle)        
class Motobike(object):
    def __init__(self, name):
        self.name = name
        self.owner = self.number = None

    def register(self, owner, number):
        if self.owner is not None:
            raise ValueError("has owner")
        self.owner = owner
        self.number = number
        owner.add_motobike(self)

    def unregister(self):
        self.owner.remove_motobike(self)
        self.owner=None
        self.number=None
