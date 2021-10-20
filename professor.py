# professor: a person who teaches at the university
# when a professor gets a new studnet, the student is saved in a set that professor owns

class Professor:
    num_courses: int
    s_add_course = 0

    def __init__(self, name):
        self.name = name
        Professor.s_add_course = Professor.s_add_course + 1
        self.num_courses = Professor.s_add_course + 1
        self.students_in_class = set()

    def to_string(self):
        s = self.name + ' courses: ' + str(self.num_courses) + '; #students = ' + str(len(self.students_in_class))
        return s

    def get_num_courses(self):
        return self.num_courses

    def get_name(self):
        return self.name

    def __eq__(self, other):
        return self.num_courses == other.num_courses

    def __hash__(self):
        return hash((self.name, self.num_courses))

    def new_student(self, student):
        self.students_in_class.add(student)

    def get_students(self):
        return list(self.students_in_class)

    def dropout_student(self, student):
        for s in self.students_in_class:
            if s == student:
                self.students_in_class.remove(student)
                return True
        print("Attempted to have student ", student, " removed from ", self, "'s course: failed")
        return False

