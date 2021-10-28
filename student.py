# student: a person who will attend a university
# when a student enrolls in a course, the course is saved in a set that student owns

class Student:
    id_number: int
    s_next_id = 0

    def __init__(self, student_name):
        self.student_name = student_name
        Student.s_next_id = Student.s_next_id + 1
        self.id_number = Student.s_next_id
        self.enrolled_courses = set()

    def to_string(self):
        string = self.student_name + ' student id: ' + str(self.id_number) + '; #enrolled_course(s) = ' + \
            str(len(self.enrolled_courses))
        return string

    def get_student_id(self):
        return self.id_number

    def get_student_name(self):
        return self.student_name
    
    def __eq__(self, other):
        return self.id_number == other.id_number

    def __hash__(self):
        return hash((self.student_name, self.id_number))

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
