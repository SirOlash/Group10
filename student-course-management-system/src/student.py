from coursemanagement.courseregistration import CourseRegistration
from coursemanagement.user import User


class Student(User):
    def __init__(self,first_name,last_name,email,password):
        super().__init__(first_name,last_name,email,password)


    def register_for_course(self,course):
        reg_manager = CourseRegistration()
        return reg_manager.register_course(self,course)






