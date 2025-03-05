from coursemanagement.course import Course
from coursemanagement.course_manager import CourseManager
from coursemanagement.user import User


class Facilitator(User):
    def __init__(self,first_name,last_name,email,password):
        super().__init__(first_name,last_name,email,password)
        self.course_manager = CourseManager()
        self._courses_created = self._load_courses()

    def _load_courses(self):
        return [
            Course(course_name, self)
            for course_name in self.course_manager.get_courses_by_facilitator(self.email)
        ]