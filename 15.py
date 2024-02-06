"""Хеширование"""
import hashlib

print(hashlib.md5('oleg'.encode('utf-8')).hexdigest())


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, person_obj):
        return isinstance(person_obj, Person) and self.name == person_obj.name
    
p1 = Person('Ivan')
p2 = Person('Ivan')

print(p1 == p2)
print(hash(p1), hash(p2))  # the same
"""ne ponyal che zza huinya i za4em nujna"""
