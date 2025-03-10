import os
import unittest

from src.models.course import Course
from src.models.users import Student, Facilitator
from src.services.course_registration import CourseRegistration, REGISTRATIONS_FILE


class MyTestCase(unittest.TestCase):

    def setUp(self):
        if os.path.exists(REGISTRATIONS_FILE):
            os.remove(REGISTRATIONS_FILE)
        self.register = CourseRegistration()
        self.facilitator = Facilitator("Bruno", "Fernandez", "Bruno@gmail.com", "password")
        self.student = Student("Odegard","mumu","mumu@gmail.com","password")
        self.course = Course("Python")

    def tearDown(self):
        if os.path.exists(REGISTRATIONS_FILE):
            os.remove(REGISTRATIONS_FILE)

    def test_that_you_can_register_a_course(self):
        result = self.register.register_course(self.student,self.facilitator,self.course)
        self.assertTrue(result)

    def test_that_each_student_can_view_their_registered_courses(self):
        self.register.register_course(self.student, self.facilitator, self.course)
        result = self.register.view_registrations_by_student(self.student)
        expected = "Course: Python, Facilitator: Bruno Fernandez, Grade: unassigned"
        self.assertEqual(expected,result)




if __name__ == '__main__':
    unittest.main()
