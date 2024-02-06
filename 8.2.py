"""Пример 2 часть"""
from datetime import datetime
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._history = []
    
    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} money')
            self._history.append([-amount, self._get_current_time()])
        else:
            print('Not enough Money.')
        self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.__balance}')
    
    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdraw'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone()}')


a = Account('oleg', 0)
a.deposit(150)
a.__balance = 100000  # пользователь не должен иметь возможности так делать -> приватизируем balance; Также к истории никто не должен обращатсья кроме пользователя
a.show_balance()  # но баланс все равно можно менять. Делаем __balance и теперь в  dir(a) мы имеем _Account__balance
print(dir(a)[0])
print(a.__dict__)
