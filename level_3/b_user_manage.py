"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str):
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            print('Данного пользователя не существует')
            

class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        self.usernames = []

if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user("user1")
    user_manager.add_user("user2")
    user_manager.add_user("user3")
    print("User Manager:")
    print("Users:", user_manager.get_users())
    
    admin_manager = AdminManager()
    print("\nAdmin Manager:")
    admin_manager.add_user("admin1")
    admin_manager.add_user("admin2")
    admin_manager.ban_username("user2")
    print("Users:", admin_manager.get_users())
    
    super_admin_manager = SuperAdminManager()
    print("\nSuper Admin Manager:")
    super_admin_manager.add_user("superadmin1")
    super_admin_manager.add_user("superadmin2")
    super_admin_manager.ban_username("admin1")
    super_admin_manager.ban_all_users()
    print("Users:", super_admin_manager.get_users())

