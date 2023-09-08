"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income
    
    def decrease_balance(self, expense: float):
        if self.balance - expense < 0:
            raise ValueError('На вашем счёте недостаточно средств')
        self.balance -= expense


if __name__ == '__main__':
    account = BankAccount('Name User', 1000.0)
    account.decrease_balance(500)
    print(f'Баланс после снятия средств: {account.balance}')
    
    try:
        account.decrease_balance(2000)
    except ValueError as e:
        print(f'Ошибка: {e}')
    
    print(f'Баланс после неудачной попытки снятия средств: {account.balance}')
