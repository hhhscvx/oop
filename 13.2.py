"""mixins"""


class FoodMixin:  # mixin - небольшое подмешивание функционала к конкретному классу путем наследования этого mixin`а
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Select favorite food!')
        print(f'I like {self.food}!')


class Person:
    def hello(self):
        print("I am Person")


class Student(FoodMixin, Person):
    food = 'Shawarma'

    def hello(self):
        print("I am Student")


s = Student()
s.get_food()
