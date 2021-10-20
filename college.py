# college provides the association between a student and a professor
# when a professor gets a new student, an instance of College is created
# this shows that a professor has a student

class College:
    def __init__(self, professor, student, college_name, class_name):
        self.professor = professor
        self.student = student
        self.college_name = college_name
        self.class_name = class_name

    def get_student(self):
        return self.student

    def get_professor(self):
        return self.professor

    def get_college_name(self):
        return self.college_name

    def get_class_name(self):
        return self.class_name

