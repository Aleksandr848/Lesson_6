class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polise

    def go(self):
        return 'Машина поехала!'

    def stop(self):
        return 'Машина остановилась!'

    def turn(self, direction):
        return f'Машина повернула {direction}!'

    def show_speed(self):
        return f'Скорость автомобиля - {self.speed} км/ч.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_polise, is_hibrid):
        super().__init__(speed, color, name, is_polise)
        self.is_hibrid = is_hibrid

    def show_speed(self):
        warning = ''
        if self.speed > 60:
            warning = 'Вы превысили скорость!'
        return f'Скорость автомобиля - {self.speed} км/ч. {warning}'

class SportCar(Car):
    def __init__(self, speed, color, name, power, is_polise):
        super().__init__(speed, color, name, is_polise)
        self.power = power

class Workcar(Car):
    def __init__(self, speed, color, name, lifting_capacity, is_polise):
        super().__init__(speed, color, name, is_polise)
        self.lifting_capacity = lifting_capacity

    def show_speed(self):
        warning = ''
        if self.speed > 40:
            warning = 'Вы превысили скорость!'
        return f'Скорость автомобиля - {self.speed} км/ч. {warning}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, department):
        super().__init__(speed, color, name, is_polise=True)
        self.department = department


car1 = TownCar(70, 'Red', 'Toyota', True, False)
car2 = SportCar(120, 'Green', 'BMW', 320, True)
car3 = Workcar(50, 'Black', 'Mack', 8000, True)
car4 = PoliceCar(70, 'Blue', 100, 'New York')
car5 = TownCar(55, 'White', 'Nissan', True, True)
car6 = Workcar(40, 'Black', 'Volvo', 12000, True)

print(car2.show_speed())
print(car1.show_speed())
print(car3.stop())
print(car4.turn('налево'))
print(car5.show_speed())
print(car6.color)
print(car6.name)
#