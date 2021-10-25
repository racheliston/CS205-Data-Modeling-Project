# course class
# university has instances of course

class Course:
    def __init__(self, course_name, professor, major):
        self.course_name = course_name
        self.professor = professor
        self.major = major

    def to_string(self):
        string = '"' + self.course_name + '" ' + self.professor + ' ' + self.major
        return string

    def get_course_name(self):
        return self.course_name

    def __eq__(self, other):
        return self.course_name == other.course_name and self.professor == other.professor

    def __hash__(self):
        return hash((self.course_name, self.professor))
        