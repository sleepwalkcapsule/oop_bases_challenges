"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    new_user = User(name="Human", username="Towel", age=22, phone="+7(999)999-99-99")
    print(f"Информация о пользователе:\nИмя - {new_user.name}.\nЛогин - {new_user.username}.\nВозраст - {new_user.age}.\nМобильный телефон - {new_user.phone}.")

