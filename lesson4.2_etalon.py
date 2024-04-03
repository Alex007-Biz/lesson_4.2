class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = "user"

    def get_user_id(self):
        return self._user_id
    def get_name(self):
        return self._name
    def get_level(self):
        __set_name__(self, owner, name)
    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = "admin"
    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь успешно добавлен в список")
    def remove_user(self, user_list, user):
        user_list.remove(user)

users = []
admin = Admin("a1", "Гоша")
user1 = User("u1", "Степа")
user2 = User("u2", "Вася")
user3 = User("u2", "Жека")


admin.add_user(users, user1)
admin.add_user(users, user2)
admin.add_user(users, user3)

for user in users:
    print(user.get_name())

admin.remove_user(users, user3)
for user in users:
    print(user.get_name())
