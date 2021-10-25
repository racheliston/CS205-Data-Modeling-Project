# enroll is the association between a course and a student
# when a student enrolls in a class, an instance of Entroll is created

class Enroll:
    def __init__(self, student, course, ):
        self.student = student
        self.course = course

    def get_course(self):
        return self.course

    def get_student(self):
        return self.student
