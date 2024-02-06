"""Порядок наследования (mro)"""


class Person:
    def hello(self):
        print('I am Person')


class Student(Person):
    def hello(self):
        print('I am Student')


class Professor(Person):
    def hello(self):
        print('I am Professor')


class Someone(Student, Professor):  # тот кто левее в наследовании тот и "главнее" для данного дочернего класса
    pass


s = Someone()
s.hello()  # метод вызывается для первого наследованного класса в Someone (Student)
print(s.__class__.mro())  # порядок родителей от более главных к менее
