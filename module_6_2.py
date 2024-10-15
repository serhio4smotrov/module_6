class Vehicle:
    _COLOR_VARIANTS = ['зелёный', 'красный', 'розовый', 'жёлтый', 'чёрный']
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color

    def get_model(self):
        return f'Модель: {self._model}'

    def get_horse_power(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horse_power()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        is_prime = True
        for i in self._COLOR_VARIANTS:
            if i.lower() == new_color.lower():
                self._color = new_color
                is_prime = False
                break
        if is_prime:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Дима', 'Toyota Mark II', 500, 'синий')
vehicle1.print_info()
print()
vehicle1.set_color('Розовый')
vehicle1.set_color('белый')
vehicle1.owner = 'Максим'
vehicle1.print_info()