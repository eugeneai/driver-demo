from components import Driver, Car
from interfaces import IDriver, IAuto
from zope.component import implementedBy

# ZCA
#
# Интерфейс - Interface - структура, описывающая то, что можно делать с ФБ.
#
# Реализация (Implementation) - *програмный код*, обычно Класс или Модуль,
# реализующий Интерфейс.
#
# Компонента (component) - обычно экземпляр Класса.
# Обслуживание, оснащение (provision) - выполнение запросов по интерфейсу,
#    как правило, экземпляр класса.
#


class Test_Driver:
    def test_Driver_implementation(self):
        assert IDriver.implementedBy(Driver)

class Test_Car:
    def setUp(self):
        self.car=Car("Traban")

    def test_car(self):
        IAuto.providedBy(self.car)


class Test_driver:
    def setUp(self):
        self.driver=Driver("John","Doe")

    def tearDown(self):
        pass

    def test_driver_provision(self):
        IDriver.providedBy(self.driver)

    def test_driver_methods(self):
        d = self.driver
        assert d.name == "John"
        assert d.familyname == "Doe"
        assert len(d.cars) == 0

    def test_fio(self):
        d = self.driver
        assert d.fio() == "John Doe"

    def test_add_car(self):
        john = self.driver
        car1 = Car("Toyota Rav IV")
        NUMBER = "y-666-kx-138-rus"
        car1.register(john, NUMBER)
        assert len(john.cars) == 1
        assert car1.owner == john
        assert car1.number == NUMBER
        car1.unregister()
        assert len(john.cars) == 0
        assert car1.owner == None
        assert car1.number == None
