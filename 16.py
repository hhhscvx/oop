"""super"""

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, surname):  # в аргументы передае включая те которые будет вызывать с super
#         super().__init__(name)  # берет функционал из род. класса связанного с name
#         self.surname = surname

# s = Student("Ivan", "Petroff")
# print(s.name, s.surname)
# print(s.__dict__)

class Person:
    def hello(self):
        print(f'Вызвано из {self.__class__.__name__}')
    
class Student(Person):
    def hello(self):
        print('Student obj.hello() is called')  # сначала пометили что из student а остальной функционал был из Person
        super().hello()  # Но пишет что вызван как-будто из Student, хотя метод из Person

s = Student()
s.hello()
