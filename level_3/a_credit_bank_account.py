"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance
        
    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount


class CreditAccount(BankAccount):
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    bank_account = BankAccount(owner_full_name='Имя Фамилия', balance=2000.0)
    print(f"Имя владельца: {bank_account.owner_full_name}")
    print(f"Баланс: {bank_account.balance}")
    bank_account.increase_balance(500.0)
    print(f"Баланс после увеличения: {bank_account.balance}")
    bank_account.decrease_balance(300.0)
    print(f"Баланс после уменьшения: {bank_account.balance}")

    credit_account = CreditAccount("Имя Фамилия", 800.0)
    print(f"Имя владельца (кредитный аккаунт): {credit_account.owner_full_name}")
    print(f"Баланс (кредитный аккаунт): {credit_account.balance}")
    is_eligible = credit_account.is_eligible_for_credit()
    print(f"Подходит ли для кредита? {is_eligible}")

