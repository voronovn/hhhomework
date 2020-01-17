class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, name, model):
        self.name = name
        self.model = model


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража

    def __init__(self, cars):
        self.cars = cars

    def __add__(self, car_to_add):
        self.cars.append(car_to_add)

    def __delete__(self, car_index):
        self.cars.remove(self.cars[car_index])

    def __getitem__(self, pos):
        return self.cars[pos]
