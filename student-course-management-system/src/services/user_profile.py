from webbrowser import register

from pythonclasswork.my_note_pad_works.student_score import student


class MainMeun:
    def __init__(self, login, register):
        self.login = login
        self.register = register

    def main_menu(self):
        print("""
              Welcome to our portal
              Enter:
              1. Login
              2. Register   
             """)

        login = int(input("Enter your choice"))
        match login:
            case 1:
                self.login()
                print("""Are you a student or facilitator?
                        Enter:
                             1. Student
                             2. Facilitator 
                        """)
                choice = int(input("Enter your choice"))
                match choice:
                    case 1:
                       self.student_login()
                    case 2:
                        self.facilitator_login()


            case 2:
                self.register()
                print("""Are you a facilitator or a student
                         Enter:
                         1. Facilitator
                         2. Student
                         """)
                register_choice = int(input("Enter your choice"))
                match register_choice:
                    case 1: self.facilitator_register()
                    case 2: self.student_register()




    def student_menu(self):
        print()

    def login(self):
        user_input = input("Are ")
        first_name = input("Enter first Name")
        if user_input == "Yes":
            self.student_menu()



