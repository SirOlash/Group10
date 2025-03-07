import tkinter as tk
from tkinter import ttk, messagebox
from models.users import Student  # Only import what you need directly
from services.authenticationservice import AuthenticationService


class CourseManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Management System")
        self.auth = AuthenticationService()
        self.current_user = None

        # Configure main container
        self.main_frame = ttk.Frame(root, padding="20 20 20 20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create notebook for different views
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.grid(row=0, column=0)

        # Create tabs
        self.login_tab = ttk.Frame(self.notebook)
        self.student_tab = ttk.Frame(self.notebook)
        self.facilitator_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.login_tab, text="Login/Register")
        self.notebook.add(self.student_tab, text="Student Dashboard")
        self.notebook.add(self.facilitator_tab, text="Facilitator Dashboard")

        self.setup_login_tab()
        self.setup_student_tab()
        self.setup_facilitator_tab()
        self.show_login_tab()

    def setup_login_tab(self):
        # Registration Section
        ttk.Label(self.login_tab, text="Registration").grid(row=0, column=0, columnspan=2)

        self.reg_type = tk.StringVar(value='student')
        ttk.Radiobutton(self.login_tab, text="Student", variable=self.reg_type, value='student').grid(row=1, column=0)
        ttk.Radiobutton(self.login_tab, text="Facilitator", variable=self.reg_type, value='facilitator').grid(row=1,
                                                                                                              column=1)

        ttk.Label(self.login_tab, text="First Name:").grid(row=2, column=0)
        self.first_name = ttk.Entry(self.login_tab)
        self.first_name.grid(row=2, column=1)

        ttk.Label(self.login_tab, text="Last Name:").grid(row=3, column=0)
        self.last_name = ttk.Entry(self.login_tab)
        self.last_name.grid(row=3, column=1)

        ttk.Label(self.login_tab, text="Email:").grid(row=4, column=0)
        self.reg_email = ttk.Entry(self.login_tab)
        self.reg_email.grid(row=4, column=1)

        ttk.Label(self.login_tab, text="Password:").grid(row=5, column=0)
        self.reg_password = ttk.Entry(self.login_tab, show="*")
        self.reg_password.grid(row=5, column=1)

        ttk.Button(self.login_tab, text="Register", command=self.register).grid(row=6, column=0, columnspan=2)

        # Login Section
        ttk.Label(self.login_tab, text="Login").grid(row=7, column=0, columnspan=2)

        ttk.Label(self.login_tab, text="Email:").grid(row=8, column=0)
        self.login_email = ttk.Entry(self.login_tab)
        self.login_email.grid(row=8, column=1)

        ttk.Label(self.login_tab, text="Password:").grid(row=9, column=0)
        self.login_password = ttk.Entry(self.login_tab, show="*")
        self.login_password.grid(row=9, column=1)

        ttk.Button(self.login_tab, text="Login", command=self.login).grid(row=10, column=0, columnspan=2)

    def setup_student_tab(self):
        ttk.Label(self.student_tab, text="Enroll in Course").grid(row=0, column=0)
        self.course_name = ttk.Entry(self.student_tab)
        self.course_name.grid(row=0, column=1)

        ttk.Label(self.student_tab, text="Facilitator Email:").grid(row=1, column=0)
        self.facilitator_email = ttk.Entry(self.student_tab)
        self.facilitator_email.grid(row=1, column=1)

        ttk.Button(self.student_tab, text="Enroll", command=self.enroll_course).grid(row=2, column=0, columnspan=2)

        # Course list
        self.course_list = ttk.Treeview(self.student_tab, columns=('Course', 'Grade'), show='headings')
        self.course_list.heading('Course', text='Course')
        self.course_list.heading('Grade', text='Grade')
        self.course_list.grid(row=3, column=0, columnspan=2)

        ttk.Button(self.student_tab, text="Logout", command=self.logout).grid(row=4, column=0, columnspan=2)

    def setup_facilitator_tab(self):
        ttk.Label(self.facilitator_tab, text="Create New Course").grid(row=0, column=0)
        self.new_course_name = ttk.Entry(self.facilitator_tab)
        self.new_course_name.grid(row=0, column=1)
        ttk.Button(self.facilitator_tab, text="Create", command=self.create_course).grid(row=0, column=2)

        # Course list
        self.facilitator_courses = ttk.Treeview(self.facilitator_tab, columns=('Course',), show='headings')
        self.facilitator_courses.heading('Course', text='Course')
        self.facilitator_courses.grid(row=1, column=0, columnspan=3)

        # Grade assignment
        ttk.Label(self.facilitator_tab, text="Assign Grades").grid(row=2, column=0)
        self.student_email = ttk.Entry(self.facilitator_tab)
        self.student_email.grid(row=2, column=1)
        self.grade_entry = ttk.Entry(self.facilitator_tab)
        self.grade_entry.grid(row=2, column=2)
        ttk.Button(self.facilitator_tab, text="Assign Grade", command=self.assign_grade).grid(row=3, column=0,
                                                                                              columnspan=3)

        ttk.Button(self.facilitator_tab, text="Logout", command=self.logout).grid(row=4, column=0, columnspan=3)

    def show_login_tab(self):
        self.notebook.hide(self.student_tab)
        self.notebook.hide(self.facilitator_tab)
        self.notebook.select(self.login_tab)

    def register(self):
        try:
            user = self.auth.register(
                self.reg_type.get(),
                self.first_name.get(),
                self.last_name.get(),
                self.reg_email.get(),
                self.reg_password.get()
            )
            messagebox.showinfo("Success", "Registration successful!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def login(self):
        try:
            self.current_user = self.auth.login(
                self.login_email.get(),
                self.login_password.get()
            )
            messagebox.showinfo("Success", f"Welcome {self.current_user.first_name}!")
            if isinstance(self.current_user, Student):
                self.notebook.select(self.student_tab)
                self.update_student_courses()
            else:
                self.notebook.select(self.facilitator_tab)
                self.update_facilitator_courses()
        except Exception as e:
            messagebox.showerror("Login Failed", str(e))

    def enroll_course(self):
        course_name = self.course_name.get()
        facilitator_email = self.facilitator_email.get()
        # Add enrollment logic here
        messagebox.showinfo("Info", "Enrollment functionality to be implemented")
        self.update_student_courses()

    def create_course(self):
        try:
            new_course = Course(self.new_course_name.get(), self.current_user)
            self.current_user.course_manager.create_course(new_course)
            messagebox.showinfo("Success", f"Course '{new_course.name}' created!")
            self.update_facilitator_courses()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def assign_grade(self):
        # Add grade assignment logic here
        messagebox.showinfo("Info", "Grade assignment functionality to be implemented")

    def logout(self):
        self.current_user = None
        self.show_login_tab()
        messagebox.showinfo("Info", "Logged out successfully")

    def update_student_courses(self):
        for item in self.course_list.get_children():
            self.course_list.delete(item)
        # Add actual course data here
        self.course_list.insert('', 'end', values=("Math 101", "A"))
        self.course_list.insert('', 'end', values=("Physics 201", "B+"))

    def update_facilitator_courses(self):
        for item in self.facilitator_courses.get_children():
            self.facilitator_courses.delete(item)
        # Add actual course data here
        self.facilitator_courses.insert('', 'end', values=("Math 101",))
        self.facilitator_courses.insert('', 'end', values=("Physics 201",))


if __name__ == "__main__":
    root = tk.Tk()
    app = CourseManagementApp(root)
    root.mainloop()

    from models.users import Course