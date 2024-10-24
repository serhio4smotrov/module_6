import math


class Figure:
    sides_count = 0
    def __init__(self,color,sides):
        self.__sides = sides
        self.__color = list(color)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        for i in (r,g,b):
            if isinstance(i,int) and 0 <= i <= 255:
                continue
            else:
                return False
        else:
            return True

    def set_color(self,r,g,b):
        self.__color = [r,g,b] if self.__is_valid_color(r,g,b) else self.__color

    def __is_valid_sides(self,*sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if isinstance(i,int) and i > 0:
                    continue
                else:
                    return False
            else:
                return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self,*new_sides):
        self.__sides = list(new_sides) if self.__is_valid_sides(*new_sides) else self.__sides


class Circle(Figure):
    sides_count = 1
    def __init__(self,color,*sides):
        self.__sides = list(sides) if len(sides) == self.sides_count else [1]
        super().__init__(color,sides=self.__sides)
        self.__radius = self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return round(math.pi * (self.__radius ** 2),2)


class Triangle(Figure):
    sides_count = 3
    def __init__(self,color,*sides):
        self.__sides = list(sides) if len(sides) == self.sides_count else [1,1,1]
        super().__init__(color,sides=self.__sides)

    def get_square(self):
        p = sum(self.__sides) / 2
        return round(math.sqrt(p*(p-self.__sides[0])*(p-self.__sides[1])*(p-self.__sides[2])),2)


class Cube(Figure):
    sides_count = 12
    def __init__(self,color,*sides):
        self.__sides = []
        if len(sides) == 1:
            for i in range(12):
                self.__sides.append(*sides)
        else:
            for i in range(12):
                self.__sides.append(1)
        super().__init__(color,sides=self.__sides)

    def get_volume(self):
        return round(self.__sides[0]**3,2)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())