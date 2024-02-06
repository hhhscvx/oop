"""аттрибуты, экземпляры, методы"""

class Person:
    name = 'Ivan'


p1 = Person()
p2 = Person()

print(f'{id(p1)}\n{id(p2)}')
print('---')
print(f'{p1.name}\n{p2.name}')
print('---')
print(f'{id(p1.name)}\n{id(p2.name)}')
print(id(Person.name))
print('---')
print(p1.__dict__, p2.__dict__)  # атрибуты берутся из родительского класса

setattr(p1, 'name', 'Oleg')
setattr(p2, 'name', 'Dima')
print('---')
print(p1.__dict__, p2.__dict__)
print('---')

p1 = Person()
p2 = Person()

Person.name = 'asdfg'

print(f'{p1.name}\n{p2.name}')
