"""property, getter, setter"""

# class Person:
#     def __init__(self, name):
#         self._name = name
    
#     def get_name(self):
#         print('From get_name()')
#         return self._name

#     def set_name(self, new_name):
#         print('From set_name()')
#         self._name = new_name
    
#     # name = property(fget=get_name, fset=set_name)  # теперь чтение или создание идет из переданных методов; Именно при обращании к p.<name> (название данной property переменной)
#     name = property()
#     name = name.getter(get_name)  # конкретно задали getter и setter; the same of `name = property(get_name)`
#     name = name.setter(set_name)

# p = Person('Dima')
# print(p.__dict__)

# print(p.name)  # From get_name()

# p.name = 'Ivan'  # From set_name()
# print(p.__dict__)
# --------------------------------------
class Person:
    def __init__(self, name):
        self._name = name

    @property  # присваиваем данной функции getter
    def name(self):
        return self._name
    
    @name.setter  # присваиваем данной функции setter
    def name(self, new_name):
        self._name = new_name
