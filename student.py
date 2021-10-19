# student: the university has instances of student

class Student:
    def __init__(self, student_name, gpa, major):
        self.student_name = student_name
        self.gpa = gpa
        self.major = major

    def to_string(self):
        s = '"' + self.student_name + '" ' + self.gpa + ' ' + self.major
        return s

    def get_title(self):
        return self.student_name

    def __eq__(self, other):
        return self.student_name == other.student_name and self.major == other.major

    def __hash__(self):
        return hash((self.student_name, self.major))
        
