import os

from src.services.course_manager import CourseManager

REGISTRATIONS_FILE = "registered_courses.txt"

class CourseRegistration:
    def __init__(self):
        self._initialize_file()

    @staticmethod
    def _initialize_file():
        if not os.path.exists(REGISTRATIONS_FILE):
            open(REGISTRATIONS_FILE, "w").close()


    @staticmethod
    def register_course(student, facilitator, course, grade ="unassigned"):
        student_name = f"{student.first_name} {student.last_name}"
        facilitator_name = f"{facilitator.first_name} {facilitator.last_name}"
        with open(REGISTRATIONS_FILE, "a") as file:
            file.write(f"{student_name},{course.course_name},{facilitator_name},{grade}\n")
        print("Registration successful!")
        return True

    @staticmethod
    def view_registrations_by_student(student):
        student_name = f"{student.first_name} {student.last_name}"
        registrations = []
        with open(REGISTRATIONS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) >= 4:
                        reg_student, course_name, facilitator_name, grade = (
                            parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()
                        )
                        if reg_student == student_name:
                            registrations.append(
                                f"Course: {course_name}, Facilitator: {facilitator_name}, Grade: {grade}")

        if registrations:
            return "\n".join(registrations)
        else:
            return "You haven't registered for any course."

        # if registrations:
        #     for reg in registrations:
        #         print(reg)
        # else:
        #     print("You haven't registered for any course.")

    @staticmethod
    def view_registrations_by_facilitator(facilitator):
        facilitator_name = f"{facilitator.first_name} {facilitator.last_name}"
        registrations = []
        with open(REGISTRATIONS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) >= 4:
                        student_name, course_name, reg_facilitator, grade = (
                            parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()
                        )
                        if reg_facilitator == facilitator_name:
                            registrations.append(f"Student: {student_name}, Course: {course_name}, Grade: {grade}")
        if registrations:
            for reg in registrations:
                print(reg)
        else:
            print("No registrations found for this facilitator.")