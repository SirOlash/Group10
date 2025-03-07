import bcrypt

# from services.courseregistration import CourseRegistration
# from src.services.course_manager import CourseManager


class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    # def _hash_password(self, password):
    #     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # def verify_password(self, password):
    #     return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.email},{self.password}"

class Student(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        # self.registration = CourseRegistration()


class Facilitator(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        # self.course_manager = CourseManager()