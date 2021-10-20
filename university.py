import college

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
		                #return self.s_university

    def __init__(self):
        self.students = set()
        self.professors = set()
        self.colleges = set()

    def add_professor(self, professor):
        self.professors.add(professor)

    def get_professors(self):
        return self.professors

    def add_student(self, student):
        self.students.add(student)

    def get_students(self):
        return self.students

    def find_professor_by_name(self, name):
            for p in self.professors:
			        if p.get_name() == name:
				            return p
		    return None

    def find_student(self, student_name):
		    students = []
		    for s in self.students:
			    if s.get_student_name() == student_name:
				    students.append(s)
		    return students


