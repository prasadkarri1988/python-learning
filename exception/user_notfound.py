class UserNotFound(Exception):

    def __init__(self, name):
        self.name = name
        super().__init__(f"User {name} not found")
