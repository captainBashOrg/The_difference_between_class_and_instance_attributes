#from reload_operators import *

print  ("История строительства")



class House:
    houses_history = []
    def __new__(cls, *args):# , **kwargs):
        instance = object.__new__(cls)
        args = args[0]
 #       print(f"Новьё  {args}")
        cls.houses_history.append(args) # доначисляем в список-историю новый ЖК
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        if isinstance(number_of_floors, House):
            self.houses_history = number_of_floors.append()

    def __del__(self):
        return print(f'{self.name} снесён, но останется в истории')

    def go_to(self, new_floor):
        if (new_floor > self.number_of_floors or new_floor < 1):
            print("Такого этажа не существует")
        else:
            for i in range (1, new_floor+1):
                print(f"Опять сломали лифт в {self.name}, ножками, этаж!  {i} из {new_floor}")
    def __len__(self):
        return   self.number_of_floors

    def __str__(self):
        return 'Название: ' + self.name + ", кол-во этажей " + str(self.number_of_floors)

    def __eq__(self, other):
        if  isinstance (other, House):
            return   self.number_of_floors == other.number_of_floors
        else:
            return False

    def __lt__(self, other):
        if  isinstance (other, House):
            return   self.number_of_floors < other.number_of_floors
        else:
            return False

    def __le__(self, other):
        if  isinstance (other, House):
            return   self.number_of_floors <= other.number_of_floors
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self


# не очень понятно, зачем, но в ТЗ есть
    def __radd__(self, value):
        return __add__(self, value)

    def __iadd__(self, value):
        return __add__(self, value)






# void main(void) {
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

h4 = House('ЖК Цветы-2', 35)
print(House.houses_history)

# Удаление объектов
# предумышленный снос зданий
print("\n"*3,"Сносим за ненадобностью ")
del h2
del h3


print(House.houses_history)

print("\n"*3,"А сейчас будут отчитываться автоматические деструкторы")


