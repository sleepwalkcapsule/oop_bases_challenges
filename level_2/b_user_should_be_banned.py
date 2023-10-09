"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def should_be_banned(self) -> bool:
        return self.last_name in SURNAMES_TO_BAN

if __name__ == '__main__':
    user_1 = User(first_name='Jay', last_name='Vaughn', age=22)
    user_2 = User(first_name='Bob', last_name='Wilhelm', age=30)
    user_3 = User(first_name='Steave', last_name='Cubin',age=29)
    user_4 = User(first_name='Alex', last_name='Santaros', age=25)
    
    if user_1.should_be_banned():
        print(f'{user_1.first_name} {user_1.last_name} should be banned')
  
    else:
        print(f'{user_1.first_name} {user_1.last_name} is allowed')
        
    if user_2.should_be_banned():
        print(f'{user_2.first_name} {user_2.last_name} should be banned')
    
    else:
        print(f'{user_2.first_name} {user_2.last_name} is allowed')
        
    if user_3.should_be_banned():
        print(f'{user_3.first_name} {user_3.last_name} should be banned')
        
    else:
        print(f'{user_3.first_name} {user_3.last_name} is allowed')
        
    if user_4.should_be_banned():
        print(f'{user_4.first_name} {user_4.last_name} should be banned')
        
    else:
        print(f'{user_4.first_name} {user_4.last_name} is allowed')
        

