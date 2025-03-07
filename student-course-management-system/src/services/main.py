import re

import bcrypt

from models.users import Facilitator, Student
from services.student_portal_service import AuthenticationService
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
                password = input("Password: ")

                try:
                    user = auth.register(
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
                    user_input = valid_name("Enter course name: ")



                    facilitator_email = input("Enter facilitator email: ")

                    print("Enrollment functionality to be implemented")

                elif choice == '2':

                    courses = current_user.registration.get_student_courses(current_user)
                    print("\nYour Courses:")
                    for course in courses:
                        print(f"- {course['course_name']} (Grade: {course['grade']})")

                elif choice == '3':
                    current_user = None
                    print("Logged out successfully")

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

                    student_email = input("Student email: ")
                    course_name = input("Course name: ")
                    grade = input("Grade: ")

                    print("Grade assignment functionality to be implemented")

                elif choice == '4':
                    current_user = None
                    print("Logged out successfully")

@staticmethod
def valid_name(prompt):
    while True:
        user_input = input(prompt).strip()
        if re.fullmatch(r'^[A-Z][a-z]+', user_input):
            return user_input

        else:
            print("Enter a valid input")


if __name__ == "__main__":
    main()