import traceback

from user_notfound import UserNotFound


class User:
    def __init__(self, user_id, name, age):
        self.id = user_id
        self.name = name
        self.age = age


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def find_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        raise UserNotFound(user_id)


manager = UserManager()

manager.add_user(User(1, "Prasad", 36))
manager.add_user(User(2, "Ram", 38))

user = None

try:
    user = manager.find_user(3)
except UserNotFound as e:
    traceback.print_exc()   # or simply print(e)
finally:
    print("Closing connection")

if user:
    print(user.name)
    print(user.age)