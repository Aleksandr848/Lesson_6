class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Имя сотрудника: {self.surname} {self.name}'

    def get_total_income(self):
        wage = self._income['wage']
        bonus = self._income['bonus']
        return f'Доход: {wage + bonus}'


worker1 = Position('Вася', 'Жуков', 'Дворник', 15000, 1000)
worker2 = Position('Вова', 'Ёжиков', 'Плотник', 40000, 5000)
worker3 = Position('Аня', 'Лукова', 'Флорист', 30000, 3000)
worker4 = Position('Ксения', 'Макарова', 'Преподаватель', 240000, 12000)

print(f'{worker1.get_full_name()}, {worker1.get_total_income()}')
print(f'{worker2.get_full_name()}, {worker2.get_total_income()}')
print(f'{worker3.get_full_name()}, {worker3.get_total_income()}')
print(f'{worker4.get_full_name()}, {worker4.get_total_income()}')
