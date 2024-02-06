"""Классы"""

class Person:
    name = 'Ivan'

print(dir(Person))

p = Person()

print(p.__class__.__name__)  # == type(p)

print(type(p))

new_person = p.__class__()

print(p)
print(new_person)
