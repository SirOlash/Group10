class Main:
    def main_menu(self):
        print("""
            Welcome to your portal. Enter
            1. Login
            2. Register
            """)

        user_choice = input("Enter your choice: ")
        match user_choice:
            case 1:
                self.login()

            case 2:
                self.register()

            case 2:
                print("Goodbye from us")
                exit()
            case _:
                print("Invalid input")