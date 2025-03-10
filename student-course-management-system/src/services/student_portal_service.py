
from registrationmanager import RegistrationManager

from src.models.users import Student


student_object = Student

class AuthenticationService:
    def __init__(self):
        self.file_manager = RegistrationManager.get_instance()
        self.users_file = "../service/users.txt"

    def register_user(self, user_type, first_name, last_name, email, password):
        existing = [line.split(',')[2] for line in self.file_manager.read_file(self.users_file)]
        if email in existing:
            raise ValueError("Email already registered")

        if user_type == 'student':
            student = Student(first_name, last_name, email, password)
            with open(self.file_manager,'a') as file:
                file.write(str(student) + "\n")

        else:
            facilitator = Facilitator(first_name,last_name,email,password)
            with open(self.file_manager,'a') as file:
                file.write(str(facilitator) + "\n")




        # self.file_manager
        # write_file(self.users_file, [user_data])
       # return Student(first_name, last_name, email, password)
       #      else Facilitator(first_name, last_name, email, password)

    def login(self, email, password):
        for line in self.file_manager.read_file(self.users_file):
            parts = line.split(',')
            if parts[2] == email:
                user = Student(parts[1], parts[2], email, parts[4]) if parts[0] == 'student' \
                    else Facilitator(parts[1], parts[2], email, parts[4])
                if user.verify_password(password):
                    return user
        raise ValueError("Invalid credentials")