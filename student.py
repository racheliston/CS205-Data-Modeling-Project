# student: a person who will attend a university
# when a student enrolls in a course, the course is saved in a set that student owns

class Student:
    gpa: float

    def __init__(self, student_name, gpa):
        self.student_name = student_name
        self.gpa = gpa
        self.enrolled_courses = set()

    def to_string(self):
        string = self.student_name + ' GPA: ' + str(self.gpa) + '; #enrolled_course(s) = ' + \
            str(len(self.enrolled_courses))
        return string

    def get_gpa(self):
        return self.gpa

    def get_student_name(self):
        return self.student_name
    
    def __eq__(self, other):
        return self.gpa == other.gpa

    def __hash__(self):
        return hash((self.student_name, self.gpa))

    def enroll_in_course(self, course):
        self.enrolled_courses.add(course)

    def get_enrollments(self):
        return list(self.enrolled_courses)

    def drop_out(self, course):
        for c in self.enrolled_courses:
            if c == course:
                self.enrolled_courses.remove(course)
                return True
        print(self, ' attempted to drop out of course ', course, ': failed')
        return False
