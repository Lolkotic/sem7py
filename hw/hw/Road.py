# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:

    def __init__(self, width, length_in_km):
        self._length_in_km = length_in_km
        self._width = width
        self.weight = 20
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length_in_km * self._width * self.weight * self.height
        print(f'We need {asphalt_mass} tons')


r = Road(25, 5)
r.asphalt_mass()
