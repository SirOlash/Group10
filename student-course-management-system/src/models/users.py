import bcrypt

# from services.courseregistration import CourseRegistration
# from src.services.course_manager import CourseManager


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

    def verify_password(self, password):
        return self.__email == password

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