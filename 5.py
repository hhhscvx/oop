"""инициализация"""

# class Person:
#     def create(self):
#         self.name = 'Ivan'  # the same of `p.name = 'Ivan` ведь self ссылается на экз.

#     def display(self):
#         print(self.name)


# p = Person()
# # p.display()  # name еще не определено
# p.create()  # создали в экземпляре name; чтоб не прописывать так всегда придуман __init__
# p.display()
# print(p.__dict__)

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

p = Person('Ivan')
print(p.__dict__)

# Создание экземпляра сост. из 2 этапов: 
    # 1) __new__() - создание самого экземпляра (конструктор)
    # 2) __init__() - инициализация экземпляра (инициализатор, присваивает переменные)
