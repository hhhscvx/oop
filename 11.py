

class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        self._full_name = None
    
    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname
        self._full_name = None

    
    @property
    def full_name(self):  # это исчисляемое свойство ведь в любой момент можно поменять name или surname через property
        if self._full_name is None:
            return f'{self._name} {self._surname}'
        return self._full_name
    
    # @property
    # def name(self):
    #     return self._name

# p = Person('Ivan')
# print(p.name)
# p.name = 'eblan'  # Traceback - свойства только для чтения это только property.getter
p = Person('Ivan', 'Ivanoff')
print(p.full_name)
print(p.__dict__)
p.surname = 'Petroff'
print(p.__dict__)
print(p.full_name)
