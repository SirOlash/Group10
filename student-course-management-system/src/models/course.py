class Course:
    def __init__(self, course_name, current_user):
        self.course_name = course_name

    def __str__(self):
        return self.course_name
