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
        self.vechicles=[]

    def fio(self):
        """
        Returns joint name and familyname
        """
        return "{} {}".format(self.name, self.familyname)

    def add(self, vechicle):
        assert IVehicle.providedBy(vechicle)
        self.vechicles.append(vechicle)

    def remove(self, vechicle):
        assert IVehicle.providedBy(vechicle)
        self.vechicles.remove(vechicle)

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
        owner.add(self)

    def unregister(self):
        self.owner.remove(self)
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
        owner.add(self)

    def unregister(self):
        self.owner.remove(self)
        self.owner=None
        self.number=None
