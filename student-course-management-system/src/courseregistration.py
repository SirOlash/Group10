import os


from coursemanagement.course_manager import CourseManager

REGISTRATIONS_FILE = "registered_courses.txt"

class CourseRegistration:
    def __init__(self, filename = REGISTRATIONS_FILE):
        self.filename = filename
        self.course_manager = CourseManager()
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("student_email,course_name,facilitator_email,facilitator_name,grade\n")

    def register_course(self, student, course):
        if not self.course_manager.course_exists(course):
            raise ValueError(f"Course {course.course_name} does not exist.")

        record = (
            f"{student.email},{course.course_name},"
            f"{course.facilitator.email},{course.facilitator.name},\n"
        )
        with open(self.filename, "a") as f:
            f.write(record)
        return f"{student.name} registered for {course.course_name}."

    def update_grade(self,student,course, grade):
        updated = False
        updated_lines = []
        with open(self.filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] == "student_email":
                    updated_lines.append(line)
                    continue
                if (
                        parts[0] == student.email
                        and parts[1] == course.course_name
                        and parts[2] == course.facilitator.email
                ):
                    parts[4] = str(grade)
                    updated_line = ",".join(parts) + "\n"
                    updated_lines.append(updated_line)
                    updated = True
                else:
                    updated_lines.append(line)

        if not updated:
            raise ValueError("Student not registered for this course.")

        with open(self.filename, "w") as file:
            file.writelines(updated_lines)

    def get_student_courses(self, student):
        courses = []
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file.readlines()[1:]:
                    parts = line.strip().split(',')
                    if parts[0] == student.email:
                        courses.append({
                            "course_name": parts[1],
                            "facilitator_name": parts[3],
                            "grade": parts[4] if parts[4] else "Not assigned"
                        })
        return courses


