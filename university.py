import enroll

# design patter -- singleton pattern
# define a static instance of the class itself and return
# that instance in a getter
#
# when a professor gets a new student, an instance of College is created
# the association between the professor and the student is shown by
# adding the student to the professor's list of students

class University:
    s_university = None

    @classmethod
    def get(self):
        if self.s_university is None:
            self.s_university = University()
        return self.s_university
        
    def __init__(self):
        self.students = set()
        self.courses = set()
        self.enrollments = set()

    def add_student(self, student):
        self.students.add(student)

    def get_students(self):
        return self.students

    def add_course(self, course):
        self.courses.add(course)

    def get_courses(self):
        return self.courses

    def find_student_by_id(self, student_id):
        for s in self.students:
            if s.get_student_id() == student_id:
                return s
        return None

    def find_student_by_name(self, student_name):
        for s in self.students:
            if s.get_student_name() == student_name:
                return s
        return None
    
    def find_course(self, course_name):
        courses = []
        for c in self.courses:
            if c.get_course_name() == course_name:
                courses.append(c)
        return courses

    def enroll_student(self, student, course):
        if not self.is_enrolled(student):
            enr = enroll.Enroll(student, course)
            student.enroll_in_course(course)
            self.enrollments.add(enr)
            return enr
        else:
            return None

    def is_enrolled(self, student):
        for e in self.enrollments:
            if e.get_student() == student:
                return True
        return False

    def show_enrollments(self):
        for e in self.enrollments:
            string = e.get_student().to_string() + ' => ' + e.get_course().to_string()
            print(string)

    def get_enrollments(self, s):
        courselist = []
        for e in self.enrollments:
            if e.get_student() == s:
                courselist.append(e.get_course())
        return courselist

    # incorrect implementation of drop out of course 

    def drop_out_incorrect_implementation(self, student, course):
        for e in self.enrollments:
            if e.get_student() == student and e.get_course() == course:
                self.enrollments.remove(e)
                return True
        return False 

    # correct implementatino of drop out of course

    def drop_out(self, student, course):
        for e in self.enrollments:
            if e.get_student() == student and e.get_course() == course:
                self.enrollments.remove(e)
                student.drop_out(course)
                return True
        return False

    def drop_out_all_courses(self):
        for s in self.students:
            s.enrolled_courses = set()
        self.enrollments = set()