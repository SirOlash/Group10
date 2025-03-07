import os
import unittest

from src.models.course import Course
from src.models.users import Facilitator
from src.services.course_manager import CourseManager, COURSES_FILE


class MyTestCase(unittest.TestCase):
    def setUp(self):
        if os.path.exists(COURSES_FILE):
            os.remove(COURSES_FILE)
        self.manager = CourseManager()
        self.facilitator = Facilitator("Bruno", "Fernandez", "Bruno@gmail.com", "password")
        self.course = Course("Python 101")

    def tearDown(self):
        if os.path.exists(COURSES_FILE):
            os.remove(COURSES_FILE)

    def test_that_course_does_not_exist_initially(self):
        self.assertFalse(self.manager.course_exists(self.facilitator, self.course))

    def test_that_you_can_add_course(self):
        result = self.manager.add_course(self.facilitator, self.course)
        self.assertTrue(result)
        self.assertTrue(self.manager.course_exists(self.facilitator, self.course))

    def test_that_you_cannot_add_same_course_twice(self):
        self.manager.add_course(self.facilitator, self.course)
        result = self.manager.add_course(self.facilitator, self.course)
        self.assertFalse(result)

    def test_that_you_can_view_all_courses(self):
        self.manager.add_course(self.facilitator, self.course)
        expected = "Facilitator: Bruno Fernandez - Course: Python 101"
        result = self.manager.view_courses()
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
