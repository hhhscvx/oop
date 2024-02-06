"""data descriptors"""

from time import time
from icecream import ic

# ic.disable()


# class Epoch:
#     def __get__(self, instance, owner_class):
#         ic(f'id of self: {id(self)}')
#         if instance is None:
#             return self  # Чтобы вызывалось именно из экземпляра
#         # ic(f'Self: {self}')  # что вызвали (Epoch)
#         # ic(f'Instance: {instance}')  # экз. из которого вызвали epoch (m = MyTime())
#         # ic(f'Owner: {owner_class}')  # класс, экземпляром которого явл. instance (MyTime)
#         return int(time())

#     def __set__(self, instance, value):
#         pass


# class MyTime:
#     epoch = Epoch()

# m = MyTime()
# ic(m.epoch)
# # ic(MyTime.epoch)  # instance = None, остальное также
# m1 = MyTime()
# ic(m1.epoch)  # id of diff instances is same

class IntDescriptor:
    def __init__(self):
        self._values = {}

    def __set__(self, instance, value):
        self._values[instance] = value
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)

class Vector:
    x = IntDescriptor()
    y = IntDescriptor()

v1 = Vector()
v2 = Vector()
v1.x = 5
ic(v1.x)
v2.x = 200
ic(v1.x)  # при изменении одного меняются оба, переделаем через values = {}
ic(v2.x)
