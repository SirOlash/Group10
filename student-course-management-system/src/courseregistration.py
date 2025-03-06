
from registrationmanager import RegistrationManager

class CourseRegistration:
    def __init__(self):
        self.file_manager = RegistrationManager.get_instance()
        self.reg_file = "registrations.txt"

    def register(self, student, course):
        data = f"{student.email},{course.name},{course.facilitator.email}"
        self.file_manager.write_file(self.reg_file, [data])

    def update_grade(self, student, course, grade):
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
        pass