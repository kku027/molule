class Car:
    def __init__(self, model, year_of_release, engine_capacity, price, mileage, number_of_wheels=4):
        self.model = model
        self.year_of_release = year_of_release
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.number_of_wheels = number_of_wheels

    def description(self):
        description = (
            f"Модель - {self.model}, Год выпуска - {self.year_of_release}, Объём двигателя - "
            f"{self.engine_capacity}, Цена - {self.price}, Пробег - {self.mileage}, Количество колёс - "
            f"{self.number_of_wheels}")
        return description

car = Car("НИВА", "2020", "2000 см3", "1500000 рублей", "42985 километров", )
print(car.description())

class Truck(Car):
    def __init__(self, model, year_of_release, engine_capacity, price, mileage, number_of_wheels=8):
        super().__init__(model, year_of_release, engine_capacity, price, mileage, number_of_wheels)
        self.subclass_car = "Грузовые"
    def description(self):
        description = (
            f"Класс машин - {self.subclass_car}, Модель - {self.model}, Год выпуска - {self.year_of_release}, Объём двигателя - "
            f"{self.engine_capacity}, Цена - {self.price}, Пробег - {self.mileage}, Количество колёс - "
            f"{self.number_of_wheels}")
        return description

truck = Truck("КАМАЗ", "2022", "6200 см3", "2450000 рублей", "2356 километров", number_of_wheels=8)
print(truck.description())
