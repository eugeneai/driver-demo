from zope.interface import Interface, Attribute


class IDriver(Interface):
    name = Attribute("Name of driver.")
    familyname = Attribute("Family name of driver.")
    cars = Attribute("List of the cars owned by driver.")
    motobikes = Attribute("List of the motobikes owned by driver.")

    def fio():
        """Returns joined name and family name.
        """

    def add_car(car):
        """
        Add a car to driver's list of cars.
        car must provide IAuto interface
        """

    def remove_car(car):
        """
        Remove car from list of cars
        """
    def add_motobike(motobike):
        """
        Add a car to driver's list of cars.
        car must provide IAuto interface
        """

    def remove_motobike(motobike):
        """
        Remove car from list of cars
        """
        

class IVehicle(Interface):

    number = Attribute("Registry number of auto")
    owner = Attribute("Reference to owner providing IDriver")

    def register(owner, number):
        """
        Register auto to owner with number.
        """
