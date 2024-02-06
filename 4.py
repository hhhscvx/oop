"""self"""

class Person:
    def hello():
        print('Hello')

print(Person.hello)  # function

p = Person()

print(p.hello)  # bound; Связанный метод с объектом hello у класса Person

Person.hello()

# p.hello()  # TypeError т.к. в метод по дефолту передается 1 аргументом self

print(type(p.hello))  # method
print(type(Person.hello))  # func

class Person:
    def hello(self):  # функция, расчитанная на то, что будет вызвана в экз. класса, методом она станет когда будет создан экз. класса
        print(self)  # self - доступ к пространству имен экземпляров из самого класса; Это ссылка на экз. класса из самого класса
