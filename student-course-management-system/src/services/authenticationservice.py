# Updated User class
class User:
    def __init__(self, first_name, last_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def verify_password(self, password):
        # Compare the provided password with the stored password
        return self.__password == password

    def __str__(self):
        return f"{self.__first_name},{self.__last_name},{self.__email},{self.__password}"


class Student(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.registration = None


class Facilitator(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.course_manager = None


# Updated AuthenticationService
import re


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

            user = next((u for u in self.get_all_users() if u.get_email() == email), None)
            if not user:
                raise ValueError("User not found")

            if not user.verify_password(password):
                raise ValueError("Invalid password")

            return user

        except Exception as e:
            raise ValueError(f"Login failed: {str(e)}")

    def user_exists(self, email):
        existing_emails = [u.get_email() for u in self.get_all_users()]
        return email in existing_emails

    def get_all_users(self):
        users = []
        try:
            with open(self.filepath, "r") as file:
                lines = file.readlines()

            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 5:
                    user_type, first_name, last_name, email, password = parts[:5]

                    if user_type == 'Student':
                        user = Student(first_name, last_name, email, password)
                    elif user_type == 'Facilitator':
                        user = Facilitator(first_name, last_name, email, password)
                    else:
                        continue

                    users.append(user)
        except FileNotFoundError:
            pass
        return users

    def save_user(self, user):
        data = f"{type(user).__name__},{user.get_first_name()},{user.get_last_name()},{user.get_email()},{user.get_password()}\n"

        try:
            with open(self.filepath, "a") as file:
                file.write(data)
        except:
            with open(self.filepath, "w") as file:
                file.write(data)