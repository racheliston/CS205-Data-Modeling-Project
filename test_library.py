import unittest
import university
import course
import student

# unit tests for University application
class TestCheckout(unittest.TestCase):
    library = None

    @classmethod
    def setUpClass(cls):
        # Only call one time
        print('setUpClass()')
        cls.library = university.University().get()

        # Define courses, professors, and majors
        course_name_1 = 'Software Engineering'
        course_name_2 = 'Computer Organization'
        course_name_3 = 'Abstract Algebra'
        professor_1 = 'Jason Hibbeler'
        professor_2 = 'Jim Eddy'
        professor_3 = 'Puck Rombach'
        major_a = 'Computer Science'
        major_b = 'Math'

        # we'll use the books and the patrons in the tests, so make them class variables
        cls.course_1 = course.Course(course_name_1, professor_1, major_a)
        cls.course_2 = course.Course(course_name_2, professor_2, major_a)
        cls.course_3 = course.Course(course_name_3, professor_3, major_b)
        cls.shannon = student.Student('Shannon')
        cls.rachel = student.Student('Rachel')
        cls.university.add_student(cls.shannon)
        cls.university.add_student(cls.rachel)
        cls.university.add_course(cls.course_1)
        cls.university.add_course(cls.course_2)
        cls.university.add_course(cls.course_3)

    @classmethod
    def tearDownClass(cls):
        # called one time, at the very end--if you need to do any final cleanup, do it here
        print('tearDownClass()')

    def setUp(self):
        # called before every test
        print('setUp()')

    def tearDown(self):
        # called after every test
        print('tearDown()')
        self.university.unenroll_from_all_courses()

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



