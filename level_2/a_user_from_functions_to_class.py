""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""

class User:
    def __init__(self, username: str, user_id: int, name: str):
        self.username = username
        self.user_id = user_id
        self.name = name


    def make_username_capitalized(self):
        return self.username.capitalize()


    def generate_short_user_description(self):
        return f'User with id {self.user_id} has {self.username} username and {self.name} name'


if __name__ == '__main__':
    user = User(username='login', user_id=1, name='first_name')
    user.username = user.make_username_capitalized()
    description = user.generate_short_user_description()
    print(description)
