import university
import student
import course

# exercise code by calling functions to ensure code is being developed correctly
# and we are testing correct functions

#--------------------------------------------------

def simple_runtime_test(UVM):

    # Define two students and add them to the university
    shannon = student.Student('Shannon')
    rachel = student.Student('Rachel')
    UVM.add_student(shannon)
    UVM.add_student(rachel)

    # Define courses, professors, and majors
    course_name_1 = 'Software Engineering'
    course_name_2 = 'Abstract Algebra'
    professor_1 = 'Jason Hibbeler'
    professor_2 = 'Puck Rombach'
    major_1 = 'Computer Science'
    major_2 = 'Math'
    course_1 = course.Course(course_name_1, professor_1, major_1)
    course_2 = course.Course(course_name_2, professor_2, major_2)
    UVM.add_course(course_1)
    UVM.add_course(course_2)

    student_to_look_for = 'Shannon'
    st = UVM.find_student_by_name(student_to_look_for)
    if st is not None:
        courses = UVM.find_course(course_name_1)
        if len(courses) > 0:
            print('enroll ' + courses[0].to_string() + ' to ' + st.to_string())
            UVM.enroll_student(st, courses[0])
        else:
            print('cannot find student in course ' + course_name_1)

        courses = UVM.find_course(course_name_2)
        if len(courses) > 0:
            print('enroll ' + st.to_string() + ' in ' + courses[0].to_string())
            UVM.enroll_student(st, courses[0])
        else:
            print('cannot find student with course name ' + course_name_2)
    else:
        print('cannot find student with name', student_to_look_for)

    print('here are the enrollments in the university:')
    UVM.show_enrollments()

    student_id_to_look_for = 101
    s = UVM.find_student_by_id(student_id_to_look_for)
    if s is not None:
        courses = UVM.get_courses(s)
        if len(courses) > 0:
            print('enroll ' + s.to_string() + ' in ' + courses[0].to_string())
        else:
            print('cannot find student with id #', student_id_to_look_for)

    print('here are the enrollments in the university:')
    UVM.show_enrollments()

#--------------------------------------------------

def main():
  my_university = university.University().get()
  simple_runtime_test(my_university)

#--------------------------------------------------

main()