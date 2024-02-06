"""Polymorphism"""


# class Person:
#     age = 1
#
#     def __add__(self, other):  # __add__ не свалился с неба, а взят из родительского класса object, мы его перопределили
#         self.age += 1  # - это и есть полиморфизм
#         return self.age
#
#
# p = Person()
# print(p + 993)

class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        raise TypeError('Wrong object!')

    def __eq__(self, other):
        return self.area == other.area


r1 = Room(3, 5)
r2 = Room(4, 7)

print(r1.area, r2.area)
print(r1 + r2)  # за r1 берется self(r1).area, а за r2 room_obj(r2).area
print('---')
r1 = Room(3, 5)
r2 = Room(5, 3)
print(r1 == r2)
