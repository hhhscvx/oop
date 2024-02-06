"""аттрибуты"""

class Person:
    name = 'Ivan'

print(dir(Person)[-1])

print(Person.__dict__)

# Person.__dict__['name'] = 'sssasdf'  # TypeError

Person.age = 22

print(Person.__dict__)

# getattr
# setattr
# delattr

print(getattr(Person, 'name'))

setattr(Person, 'birth', '123')

print(Person.__dict__)

delattr(Person, 'birth')

print(Person.__dict__)

class Person:
    name = 'Ivan'

    def hello():
        print("Hello")

Person.hello()
print(Person.__dict__)
