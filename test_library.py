import unittest
import university
import course
import student

# unit tests for University application
class TestEnroll(unittest.TestCase):
    library = None

    @classmethod
    def setUpClass(cls):
        # Only call one time
        print('setUpClass()')
        cls.university = university.University().get()

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
        print('tearDownClass()')

    def setUp(self):
        print('setUp()')

    def tearDown(self):
        print('tearDown()')
        self.university.drop_out_all_courses()
        
	# -------------------------------------------------------------

    def test_drop_out_incorrect(self):
        # this tests the incorrect version of enroll_student in a course: this test will fail

        # enroll Shannon in a course
        self.university.enroll_student(self.shannon, self.course_1)
        # shannon drops her course--should return True
        rc = self.university.drop_out_incorrect_implementation(self.shannon, self.course_1)
        self.assertTrue(rc)

        # try to drop out of the course again--should return False
        rc = self.university.drop_out_incorrect_implementation(self.shannon, self.course_1)
        self.assertFalse(rc)

        # check that the university shows that shannon is not enrolled in any courses
        courses = self.university.get_enrollments(self.shannon)
        self.assertEqual(len(courses), 0)

        # check that shannon shows no enrollments
        # right now, this code is failing, because my code is incorrect--
        # I'm returning to the university but not to Student
        courses = self.shannon.get_enrollments()
        self.assertEqual(len(courses), 0)

    # -------------------------------------------------------------

    def test_drop_out_correct(self):
        # this tests the correct implemenation of unenroll student: it will succeeed

        # enroll shannon in a course
        self.university.enroll_student(self.shannon, self.course_1)
        # return shannon's courses--should return True
        rc = self.university.drop_out(self.shannon, self.course_1)
        self.assertTrue(rc)

        # try to return the same course again--should return False
        rc = self.university.drop_out(self.shannon, self.course_1)
        self.assertFalse(rc)

        # check that the university shows that shannon has no enrollments
        courses = self.university.get_enrollments(self.shannon)
        self.assertEqual(len(courses), 0)

        # check that shannon shows no enrollments
        # this will pass
        courses = self.shannon.get_enrollments()
        self.assertEqual(len(courses), 0)

    # -------------------------------------------------------------

    def test_is_enrolled(self):
        # enroll shannon in a course
        self.university.enroll_student(self.shannon, self.course_1)

        # return shannon's courses--should return True
        e = self.university.is_enrolled(self.shannon)
        self.assertTrue(e)

        # return shannon's courses--should return True
        rc = self.university.drop_out(self.shannon, self.course_1)
        self.assertTrue(rc)

        e = self.university.is_enrolled(self.shannon)
        self.assertFalse(e)

    # -------------------------------------------------------------

    def test_enroll_one(self):
        # enroll rachel in a course
        e = self.university.enroll_student(self.rachel, self.course_2)
        self.assertIsNotNone(e)

        # check that the university shows one course is enrolled to rachel
        courses = self.university.get_enrollments(self.rachel)
        self.assertEqual(len(courses), 1)

        # check that the course rachel is enrolled in is course_2
        if len(courses) == 1:
            self.assertEqual(courses[0], self.course_2)

        # check that rachel shows she is enrolled in one course
        courses = self.rachel.get_enrollments()
        self.assertEqual(len(courses), 1)

         # check that the course rachel is enrolled in is course_2
        if len(courses) == 1:
            self.assertEqual(courses[0], self.course_2)

	# -------------------------------------------------------------

    def test_enroll_two(self):
        # check that the university has no courses enrolled in by rachel
        courses = self.university.get_enrollments(self.rachel)
        self.assertEqual(len(courses), 0)

        # enroll rachel in a course
        e = self.university.enroll_student(self.rachel, self.course_1)

        # check that the university has rachel enrolled in one course
        courses = self.university.get_enrollments(self.rachel)
        self.assertEqual(len(courses), 1)

        # check to see if the course rachel is enrolled in is course_1
        if len(courses) == 1:
            self.assertEqual(courses[0], self.course_1)

        # check that rachel shows she is enrolled in one course
        courses = self.rachel.get_enrollments()
        self.assertEqual(len(courses), 1)

        # check to see if the course rachel is enrolled in is course_1
        if len(courses) == 1:
            self.assertEqual(courses[0], self.course_1)

	# -------------------------------------------------------------

    def test_drop_all_courses(self):
        # enroll rachel in a course
        e = self.university.enroll_student(self.rachel, self.course_1)

        # enroll rachel in another course
        e = self.university.enroll_student(self.rachel, self.course_2)

        # drop rachel out of all courses
        e = self.university.drop_out_all_courses()

        # check that rachel shows she is not enrolled in any courses
        courses = self.rachel.get_enrollments()
        self.assertEqual(len(courses), 0)

	# -------------------------------------------------------------

