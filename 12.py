"""Наследование"""


# class Person:
#     age = 0

#     def hello(self):
#         print("Hello")


# class Student(Person):
#     pass


# s = Student()
# print(dir(s))  # имеет св-ва из родительского класса
# print(s.__dict__)
# print(Student.__dict__)
# --------------------------
# class IntelCpu:
#     cpu_socket = 1151
#     name = 'Intel'
#
#
# class I7(IntelCpu):
#     pass
#
#
# class I5(IntelCpu):
#     pass
#
#
# i5 = I5()
# i7 = I7()
#
# # print(isinstance(i5, IntelCpu))  # isinstance - проверка наследования
# # print(isinstance(IntelCpu, object))
# #
# # print(type(i5).__name__)
#
#
# class One:
#     pass
#
#
# class Two(One):
#     pass
#
#
# class Three(Two):
#     pass
#
#
# print(issubclass(Three, Two))
# print(issubclass(Three, One))
# --------------------------
# class Person:
#     def hello(self):
#         print("I am Person")
#
#
# class Student(Person):
#     def goodbye(self):  # расширение функциональности родительского класса
#         print('Goodbye')
#
#
# p = Person()
# s = Student()
# p.hello()
# s.goodbye()
# --------------------------
class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello from {self.name}!')


class Student(Person):
    pass


s = Student('Ivan')
s.hello()
