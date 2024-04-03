class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self._users_list = []

    def add_user(self, user):
        self._users_list.append(user)

    def remove_user(self, user):
        self._users_list.remove(user)

    def get_users_list(self):
        return self._users_list

# Пример использования классов
user1 = User(1, 'John Doe')
admin1 = Admin(2, 'Alice Smith')

print(user1.get_name())
print(admin1.get_access_level())

admin1.add_user(user1)
users_list = admin1.get_users_list()
for user in users_list:
    print(user.get_name())


