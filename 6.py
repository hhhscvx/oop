"""staticmethods"""

class Person:
    def hello(self):
        print("Hello")
    
    @staticmethod
    def goodbye():
        print('Goodbye')

# p = Person()
# p.goodbye()  # staticmethod не передает self и ошибки нет
a = Person()
b = Person()

a.hello()
a.goodbye()
print('---')
print(id(a.hello))
print(id(b.hello))
print('---')
print(id(a.goodbye))  # the same
print(id(b.goodbye))  # staticmethod`ы глобальны для всех экз. класса
print('---')
print(type(a.hello))  # method
print(type(a.goodbye))  # func
