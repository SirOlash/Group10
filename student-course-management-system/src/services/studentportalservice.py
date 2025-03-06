from database.userdatabase import UserFileManager
from models.users import UserCreator


class AuthenticationService:
    user_database = UserFileManager("users.txt")

    def register(self, user_type, email, password):
        user = UserCreator.create(user_type, email, password)
        self.user_database.save(user)
        return user

    def login(self, email, password):
        users = [user for user in self.user_database.scan_through_file() if user.email == email]
        if not users:
            raise ValueError("User not found")
        if users[0].password != password:
            raise ValueError("Invalid password")
        return users[0]