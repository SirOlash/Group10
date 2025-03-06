
from registrationmanager import RegistrationManager
from models.users import Student, Facilitator

class AuthenticationService:
    def __init__(self):
        self.file_manager = RegistrationManager.get_instance()
        self.users_file = "users.txt"

    def register(self, user_type, first_name, last_name, email, password):
        existing = [line.split(',')[2] for line in self.file_manager.read_file(self.users_file)]
        if email in existing:
            raise ValueError("Email already registered")

        user_data = f"{user_type},{first_name},{last_name},{email},{password}"

        self.file_manager.write_file(self.users_file, [user_data])

        return Student(first_name, last_name, email, password) if user_type == 'student' \
            else Facilitator(first_name, last_name, email, password)

    def login(self, email, password):
        for line in self.file_manager.read_file(self.users_file):
            parts = line.split(',')
            if parts[3] == email:
                user = Student(parts[1], parts[2], email, parts[4]) if parts[0] == 'student' \
                    else Facilitator(parts[1], parts[2], email, parts[4])
                if user.verify_password(password):
                    return user
        raise ValueError("Invalid credentials")