import os
from models.users import Student, Facilitator
import bcrypt


class UserFileManager:
    def __init__(self, file_path):
        self.file_path = file_path


    def save(self, user):

        existing_mail = [user.email for user in self.scan_through_file()]
        if user.email in existing_mail:
            raise ValueError("Email already exists")

        password_bytes = user.password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        hashed_str = hashed_password.decode('utf-8')

        data = f"{type(user).__name__},{user.email},{hashed_str}"
        self.write_file(
            self.file_path,
            self.read_file(self.file_path) + [data]
        )

    def scan_through_file(self):
        users = []
        for line in self.read_file(self.file_path):
            user_type, email, password_hash = line.split(',')
            if user_type == 'Student':
                users.append(Student(email, password_hash))
            elif user_type == 'Facilitator':
                users.append(Facilitator(email, password_hash))
        return users

    def read_file(self, file_path):
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r') as f:
            return f.read().splitlines()

    def write_file(self, file_path, data):
        with open(file_path, 'a' if os.file_path.exists(file_path) else 'w') as f:
            f.write('\n'.join(data) + '\n')

