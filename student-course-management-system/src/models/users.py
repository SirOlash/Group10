from models.users import Student, Instructor

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Student(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.enrolled_courses = []

class Instructor(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.created_courses = []

class UserCreator:
    @staticmethod
    def create(user_type, email, password):
        if user_type == 'student':
            return Student(email, password)
        elif user_type == 'instructor':
            return Instructor(email, password)
        raise ValueError("Invalid user type")