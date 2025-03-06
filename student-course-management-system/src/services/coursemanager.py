
from registrationmanager import RegistrationManager



class CourseManager:
    def __init__(self):
        self.registrationmanager = RegistrationManager.get_instance()
        self.courses_file = "courses.txt"

    def create_course(self, course):
        existing = self.registrationmanager.read_file(self.courses_file)
        if any(course.name in line for line in existing):
            raise ValueError("Course already exists")
        data = f"{course.name},{course.facilitator.email}"
        self.registrationmanager.write_file(self.courses_file, [data])

    def get_courses(self, facilitator):
        return [line.split(',')[0] for line in self.registrationmanager.read_file(self.courses_file)
                if line.split(',')[1] == facilitator.email]