import re
import time

from models.users import Facilitator, Student
from services.authenticationservice import AuthenticationService
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
        if current_user is None:
            display_main_menu()
            choice = input("Enter choice: ")

            if choice == '1':
                user_type = input("Are you a (1) Student or (2) Facilitator? ")
                first = valid_name("First name: ")
                last = valid_name("Last name: ")
                email = valid_email("Email: ").lower()
                password = input("Password: ")

                try:
                    auth.register(
                        'student' if user_type == '1' else 'facilitator',
                        first, last, email, password
                    )
                    loading_screen("Registering")
                    print("Registration successful!")
                    # Don't set current_user here, so we return to main menu
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == '2':
                email = input("Email: ")
                password = input("Password: ")
                try:
                    current_user = auth.login(email, password)
                    print(f"Welcome {current_user.get_first_name()}!")
                except Exception as e:
                    print(f"Login failed: {e}")

            elif choice == '3':
                print("Exiting system...")
                break
            else:
                print("Invalid choice, please try again.")

        else:
            if isinstance(current_user, Student):
                display_student_menu()
                choice = input("Enter choice: ")

                if choice == '1':
                    course_name = valid_name("Enter course name: ")
                    facilitator_email = input("Enter facilitator email: ")

                    print(f"Attempting to enroll in {course_name} with facilitator {facilitator_email}")
                    print("Enrollment functionality to be implemented")

                elif choice == '2':
                    if current_user.registration:
                        courses = current_user.registration.get_student_courses(current_user)
                        print("\nYour Courses:")
                        for course in courses:
                            print(f"- {course['course_name']} (Grade: {course['grade']})")
                    else:
                        print("No courses registered yet.")

                elif choice == '3':
                    current_user = None
                    print("Logged out successfully")
                else:
                    print("Invalid choice, please try again.")

            elif isinstance(current_user, Facilitator):
                display_facilitator_menu()
                choice = input("Enter choice: ")

                if choice == '1':
                    course_name = input("Enter course name: ")
                    try:
                        if current_user.course_manager:
                            new_course = Course(course_name, current_user)
                            current_user.course_manager.create_course(new_course)
                            print(f"Course '{course_name}' created successfully!")
                        else:
                            print("Course manager not initialized.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif choice == '2':
                    if current_user.course_manager:
                        courses = current_user.course_manager.get_courses(current_user)
                        print("\nYour Courses:")
                        for course in courses:
                            print(f"- {course}")
                    else:
                        print("No courses created yet.")

                elif choice == '3':
                    student_email = input("Student email: ")
                    course_name = input("Course name: ")
                    grade = input("Grade: ")

                    print(f"Assigning grade {grade} to student {student_email} for course {course_name}")
                    print("Grade assignment functionality to be implemented")

                elif choice == '4':
                    current_user = None
                    print("Logged out successfully")
                else:
                    print("Invalid choice, please try again.")


def valid_email(prompt):
    while True:
        user_input = input(prompt).strip()
        if re.fullmatch(r'^[a-zA-Z0-9._%+-]+@+[a-zA-Z]+\.com$', user_input):
            return user_input
        else:
            print("\033[91mInvalid email. Please try again.\033[0m")

def valid_name(prompt):
    while True:
        user_input = input(prompt).strip()
        if re.fullmatch(r'^[A-Za-z]+', user_input):
            return user_input
        else:
            print("\033[91mInvalid input. Please try again.\033[0m")

def loading_screen(message):
    print(message, end='')
    for index in range(1, 6):
        print(">", end='')
        time.sleep(1)
    print()

r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


if __name__ == "__main__":
    main()