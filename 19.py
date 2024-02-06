"""more descriptor practice"""

from icecream import ic


class ValidString:
    def __set_name__(self, owner_class, property_name):
        ic('__set__')
        self.property_name = property_name
        # ic(owner_class)  # класс из которого создаем экземпляр
        # ic(property_name)  # имя экземпляра

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(
                f'{self.property_name} should be a string, but `{type(value).__name__}` was passed')
        key = '_' + self.property_name
        setattr(instance, key, value)  # после проверки задает _<name> и сохраняет в атрибуты
        # instance.__dict__[self.property_name] = value  # альтернатива setattr
    
    def __get__(self, instance, owner):
        ic('__get__')
        if instance is None:
            return self
        key = '_' + self.property_name
        return getattr(instance, key, None)  # выдает атрибут по _<name>
        # return instance.__dict__.get(self.property_name, None)  # альтернатива getattr


class Person:
    name = ValidString()  # при операциях с даннооой переменной будет проверяться условие в set
    surname = ValidString()


p = Person()
p.name = "Ivan"
p.surname = "Petroff"
ic(p.__dict__)
ic(p.name)
