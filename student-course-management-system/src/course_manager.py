import os

COURSES_FILE = "courses.txt"

class CourseManager:
    def __init__(self, filename=COURSES_FILE):
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("facilitator_email,course_name\n")

    def course_exists(self, course):
        if not os.path.exists(self.filename):
            return False
        with open(self.filename, "r") as f:
            for line in f.readlines()[1:]:  # Skip header
                facilitator_email, course_name = line.strip().split(',')
                if (
                    course_name == course.course_name
                    and facilitator_email == course.facilitator.email
                ):
                    return True
        return False

    def get_courses_by_facilitator(self, facilitator_email):
        courses = []
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f.readlines()[1:]:
                    fac_email, course_name = line.strip().split(',')
                    if fac_email == facilitator_email:
                        courses.append(course_name)
        return courses