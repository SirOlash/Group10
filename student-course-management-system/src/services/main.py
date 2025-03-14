import time

from models.users import Facilitator, Student
from services.authenticationservice  import AuthenticationService
from models.course import Course



def display_main_menu():
    print("\nStudent Course Management System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")


def display_student_menu():
    print("\nStudent Dashboard")
    print("1. Enroll in Course")
    print("2. View My Courses")
    print("3. Logout")


def display_facilitator_menu():
    print("\nFacilitator Dashboard")
    print("1. Create New Course")
    print("2. View My Courses")
    print("3. Assign Grades")
    print("4. Logout")


def main():
    auth = AuthenticationService()
    current_user = None

    while True:
        if not current_user:
            display_main_menu()
            choice = input("Enter choice: ")

            if choice == '1':

                user_type = input("Are you a (1) Student or (2) Facilitator? ")
                first = input("First name: ")
                last = input("Last name: ")
                email = input("Email: ").lower()
                password = input("Pas1sword: ")

                try:
                    current_user = auth.register(
                        'student' if user_type == '1' else 'facilitator',
                        first, last, email, password
                    )
                    print("Registration successful!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == '2':

                email = input("Email: ")
                password = input("Password: ")
                try:
                    current_user = auth.login(email, password)
                    print(f"Welcome {current_user.first_name}!")
                except Exception as e:
                    print(f"Login failed: {e}")

            elif choice == '3':
                print("Exiting system...")
                break

        else:

            if isinstance(current_user, Student):
                display_student_menu()
                choice = input("Enter choice: ")


                if choice == '1':
                    course_name = input("Enter course name: ").strip()
                    facilitator_email = input("Enter facilitator email: ").lower()


                    try:

                        all_users = auth.get_all_users()
                        facilitator = next(
                            (u for u in all_users if isinstance(u, Facilitator) and u.email == facilitator_email),
                            None
                        )

                        if not facilitator:
                            print("Error: Facilitator not found!")
                            continue

                        course = Course(course_name, facilitator)


                        if current_user.registration.register_course(current_user, facilitator, course):
                            print(f"Successfully enrolled in {course_name}!")
                        else:
                            print("Enrollment failed!")

                    except Exception as e:
                        print(f"Error: {str(e)}")

            elif isinstance(current_user, Facilitator):
                display_facilitator_menu()
                choice = input("Enter choice: ")

                if choice == '1':

                    course_name = input("Enter course name: ")
                    try:
                        new_course = Course(course_name, current_user)
                        current_user.course_manager.create_course(new_course)
                        print(f"Course '{course_name}' created successfully!")
                    except Exception as e:
                        print(f"Error: {e}")

                elif choice == '2':

                    courses = current_user.course_manager.get_courses(current_user)
                    print("\nYour Courses:")
                    for course in courses:
                        print(f"- {course}")


                elif choice == '3':

                    student_email = input("Student email: ").lower()

                    course_name = input("Course name: ").strip()

                    grade = input("Grade: ").strip().upper()

                    try:
                        all_users = auth.get_all_users()

                        student = next(

                            (u for u in all_users if isinstance(u, Student) and u.email == student_email),

                            None

                        )

                        if not student:
                            print("Error: Student not found!")

                            continue

                        course = Course(course_name, current_user)

                        if current_user.course_manager.update_grade(student, course, grade):

                            print(f"Grade {grade} assigned successfully!")

                        else:

                            print("Grade assignment failed!")


                    except Exception as e:

                        print(f"Error: {str(e)}")

    def loading_screen(message):
        print(message, end='')
        for index in range(1, 6):
            print(">", end='')
            time.sleep(1)
        print()

if __name__ == "__main__":
    main()