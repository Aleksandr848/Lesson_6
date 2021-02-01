class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}. Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title}. Запуск отрисовки ручкой.')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title}. Запуск отрисовки карандашом.')


class Handle(Stationery):

    def draw(self):
        print(f'{self.title}. Запуск отрисовки маркером.')


work1 = Stationery('Псина')
work2 = Pen('Кот')
work3 = Pencil('Лось')
work4 = Handle('Рассвет')

work1.draw()
work2.draw()
work3.draw()
work4.draw()
#