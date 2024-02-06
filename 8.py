"""Пример 1 часть"""
from datetime import datetime
import pytz  # pytimezone

WHITE = '\033[00m'  # write to me please ecma-48 color codes (чату гпт написать)
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:  # Bank account
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []
    
    @staticmethod
    def _get_current_time():  # экземпляр класса не используется, метод просто возвращает время -> логично сделать его staticmethod`ом
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):  # получение денег
        self.balance += amount
        self.show_balance()
        self.history.append([amount, self._get_current_time()])

    def withdraw(self, amount):  # оплата, вывод денег
        if self.balance > amount:
            self.balance -= amount
            print(f'You spent {amount} money')
            self.history.append([-amount, self._get_current_time()])
        else:
            print('Not enough Money.')
        self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.balance}')
    
    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdraw'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone()}')


a = Account('oleg', 0)
a.show_balance()
a.deposit(100)
a.withdraw(50)
a.deposit(150)
a.withdraw(120)
# print(pytz.utc.localize(datetime.utcnow()).astimezone().isoformat())  # UTC (Всемирное Координированное Время)
a.show_history()
