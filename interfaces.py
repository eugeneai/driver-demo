from zope.interface import Interface, Attribute


class IDriver(Interface):
    name = Attribute("Name of driver.")
    familyname = Attribute("Family name of driver.")
    vechicles = Attribute("List of the vechicles owned by driver.")

    def fio():
        """Returns joined name and family name.
        """

    def add(vechicle):
        """
        Add a vechicle to driver's list of vechicles.
        car must provide IAuto interface
        """

    def remove(vechicle):
        """
        Remove vechicle from list of vechicles
        """


class IVehicle(Interface):

    number = Attribute("Registry number of auto")
    owner = Attribute("Reference to owner providing IDriver")

    def register(owner, number):
        """
        Register auto to owner with number.
        """
