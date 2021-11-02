import unittest
import university
import course
import student

# unit tests for University application

class TestEnroll(unittest.TestCase):
    university = None

    # static member function setUpClass() - called once before any tests run
    # refer to member variables through this function
    @classmethod
    def tearDownClass(cls):
        print('setUpClass()')
        cls.university = university.University().get()

        # create some students and courses
        course_name_1 = 'Course One'
        course_name_2 = 'Course Two'
        course_name_3 = 'Course Three'
        student_a = 'Student A'
        student_b = 'Student B'
        student_c = 'Student C'

        # make them class variables
        cls.course_1 = course.Course(course_name_1, student_a, 'Major D')
        cls.course_2 = course.Course(course_name_2, student_b, 'Major E')
        cls.course_3 = course.Course(course_name_3, student_c, 'Major F')

        cls.shannon = student.Student('Shannon')
        cls.rachel = student.Student('Rachel')

        cls.university.add_student(cls.shannon)
        cls.university.add_student(cls.rachel)

        cls.university.add_course(cls.course_1)
        cls.university.add_course(cls.course_2)
        cls.university.add_course(cls.course_3)

    # static member function tearDownClass() - any cleanup needed 
    @classmethod
    def tearDownClass(cls):
        # called one time, at the very end--if you need to do any final cleanup, do it here
        print('tearDownClass()')
        
    def setUp(self):
        print('setUp()')
    
    def tearDown(self):
		# called after every test
        print('tearDown()')
        self.university.return_all_books()

	# -------------------------------------------------------------



