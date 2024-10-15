class Vehicle:
    __COLOR_VARIANTS = ['зелёный', 'красный', 'розовый', 'жёлтый', 'чёрный']
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Дима', 'Toyota Mark II', 500, 'синий')
vehicle1.print_info()
print()
vehicle1.set_color('Розовый')
vehicle1.set_color('белый')
vehicle1.owner = 'Максим'
vehicle1.print_info()