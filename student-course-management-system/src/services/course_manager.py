import os

from src.models.course import Course
from src.models.users import Facilitator

COURSES_FILE = "courses.txt"

class CourseManager:
    def __init__(self):
        self._initialize_file()

    @staticmethod
    def _initialize_file():
        if not os.path.exists(COURSES_FILE):
            open(COURSES_FILE, "w").close()

    @staticmethod
    def course_exists(facilitator : Facilitator, course: Course):
        facilitator_name = f"{facilitator.get_first_name} {facilitator.get_last_name}"
        with open(COURSES_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) >= 2:
                        stored_facilitator, stored_course = parts[0].strip(), parts[1].strip()
                        if stored_facilitator == facilitator_name and stored_course == course.course_name:
                            return True
        return False

    def add_course(self,facilitator : Facilitator, course: Course):
        if self.course_exists(facilitator, course):
            print("This facilitator has already created this course!")
            return False
        else:
            facilitator_name = f"{facilitator.get_first_name} {facilitator.get_last_name}"
            with open(COURSES_FILE, "a") as file:
                file.write(f"{facilitator_name},{course.course_name}\n")
            print("Course added successfully!")
            return True

    @staticmethod
    def view_courses():
        courses = []
        with open(COURSES_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) >= 2:
                        facilitator_name = parts[0].strip()
                        course_name = parts[1].strip()
                        # courses.append((facilitator_name, course_name))
                        courses.append(f"Facilitator: {facilitator_name} - Course: {course_name}")

        if courses:
            return "\n".join(courses)
        else:
            return "no courses created yet"

        # if courses:
        #     print("Available courses:")
        #     for facilitator_name, course_name in courses:
        #         print(f"Facilitator: {facilitator_name} - Course: {course_name}")
        # else:
        #     print("no courses created yet")


