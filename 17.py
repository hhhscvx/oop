"""non-data descriptors"""

# class Person:
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname
#         self._full_name = None
    
#     @property  # в этом коде много повторяется, перепишем иначе
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
#         self._full_name = None
    
#     @property
#     def surname(self):
#         return self._surname

#     @surname.setter
#     def surname(self, new_surname):
#         self._surname = new_surname
#         self._full_name = None
# -----------------------------------------
# class StringD:
#     def __init__(self, value=None) -> None:
#         if value:
#             self.set(value)
    
#     def set(self, value):  # Дескрипторы
#         self._value = value

#     def get(self):
#         return self._value

# class Person:
#     def __init__(self, name, surname) -> None:
#         self.name = StringD(name)
#         self.surname = StringD(surname)

# p = Person("Ivan", "Ivanoff")
# print(p.name)
# print(p.name.get())
# p.name.set("Petr")
# print(p.name.get())
# -----------------------------------------
from time import time
from random import choice


class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())

class MyTime:
    epoch = Epoch()

m = MyTime()

# print(m.epoch)


class Choice:
    def __init__(self, *choice):
        self._choice = choice
    
    def __get__(self, instance, owner):
        return choice(self._choice)

class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice('Heads', 'Tails')
    rock_paper_scissors = Choice('Rock', 'Paper', 'Scissors')


# class Game:
#     @property
#     def rock_paper_scissors(self):  # у каждой игры аналогичный код, это избыточно
#         return choice(['Rock', 'Paper', 'Scissors'])
    
#     @property
#     def flip(self):
#         return choice(['Heads', 'Tails'])
    
#     @property
#     def dice(self):
#         return choice(range(1, 7))

d = Game()
print(d.rock_paper_scissors)
print(d.flip)
print(d.flip)
for i in range(3):
    print(d.dice)
