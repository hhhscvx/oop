"""Области видимости классов и @classmethod"""

# name = 'Ivan'

# class Person:
#     name = 'Dima'  # у переменной своя локальная видимость, а у print_name своя другая локальная видимость

#     def print_name(self):
#         print(self.name)


# p = Person()
# print(p.__dict__)
# p.print_name()

# p.name = 'sadfg'
# print('Instance dict:', p.__dict__)

# print('Person name:', Person.name)  # имя класса неизменно, из экземпляра его можно только читать
# ------------------------------------------------
# class Person:
#     name = 'Dima'

#     @classmethod
#     def change_name(cls, name):  # cls - класс
#         cls.name = name  # присваиваем переменной класса name новое значение из этого метода

# p = Person()
# print(p.__dict__)
# p.change_name('ofc da')  # переменной name класса присвоено asd
# print('Person name:', Person.name)
# ------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name
    
    @classmethod  # вариант использования - альтернативная инициализация
    def second_init(cls, second_name):
        return cls(name=second_name)

p = Person('Igor')
print(p.__dict__)

p = Person.second_init('Mepgar')
print(p.__dict__)
