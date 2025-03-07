import bcrypt
import re

from models.users import Student, Facilitator


class AuthenticationService:
    filepath = "users.txt"

    def register(self, user_type, first_name, last_name, email, password):
        try:
            if user_type not in ['student', 'facilitator']:
                raise ValueError(f"Invalid user type: You are neither Student or Facilitator {user_type}")

            if not first_name.isalpha():
                raise ValueError("First name should contain only alphabetic characters")

            if not last_name.isalpha():
                raise ValueError("Last name should contain only alphabetic characters")

            email_pattern = r'^[a-zA-Z0-9._%+-]+@+[a-zA-Z]+\.com$'
            if not re.match(email_pattern, email):
                raise ValueError("Invalid email format. Please enter a valid email address")

            if self.user_exists(email):
                raise ValueError("Email already registered")

            if not isinstance(password, str):
                raise ValueError("Password must be a string")

            if len(password) < 1:
                raise ValueError("Password must be at least 1 character long")


            if user_type == 'student':
                user = Student(first_name, last_name, email, password)
            else:
                user = Facilitator(first_name, last_name, email, password)

            self.save_user(user)
            return user

        except Exception as e:
            raise ValueError(f"Registration failed: {str(e)}")

    def login(self, email, password):
        try:
            email_pattern = r'^[a-zA-Z0-9._%+-]+@+[a-zA-Z]+\.com$'
            if not re.match(email_pattern, email):
                raise ValueError("Invalid email format")

            user = next((u for u in self.get_all_users() if u.email == email), None)
            if not user:
                raise ValueError("User not found")

            if not user.verify_password(password):
                raise ValueError("Invalid password")

            return user

        except Exception as e:
            raise ValueError(f"Login failed: {str(e)}")

    def user_exists(self, email):
        existing_emails = [u.email for u in self.get_all_users()]
        return email in existing_emails

    def get_all_users(self):
        users = []
        try:
            with open(self.filepath, "r") as file:
                lines = file.readlines()

            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 5:
                    if parts[0] == 'Student':
                        users.append(Student(parts[1], parts[2], parts[3], parts[4]))
                    elif parts[0] == 'Facilitator':
                        users.append(Facilitator(parts[1], parts[2], parts[3], parts[4]))
        except FileNotFoundError:
            pass
        return users

    def save_user(self, user):
        password = user.password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        hashed_str = hashed_password.decode('utf-8')

        data = f"{type(user).__name__},{user.first_name},{user.last_name},{user.email},{hashed_str}\n"

        try:
            with open(self.filepath, "a") as file:
                file.write(data)
        except:
            with open(self.filepath, "w") as file:
                file.write(data)