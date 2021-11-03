import university
import student
import course

# exercise code by calling functions to ensure code is being developed correctly
# and we are testing correct functions

#--------------------------------------------------

def simple_runtime_test(the_university):
    shannon = student.Student('Shannon')
    rachel = student.Student('Rachel')
    the_university.add_student(shannon)
    the_university.add_student(rachel)

    course_name_1 = 'Software Engineering'
    course_name_2 = 'Computer Organization'
    course_1 = course.Course(course_name_1, 'Jason Hibbeler', 'Computer Science')
    course_2 = course.Course(course_name_2, 'Jim Eddy', 'Computer Science')
    the_university.add_course(course_1)
    the_university.add_course(course_2)

    student_to_look_for = 'Shannon'
    s = the_university.find_student_by_name(student_to_look_for)
    if s is not None:
        courses = the_university.find_course(course_name_1)
        if len(courses) > 0:
            print('enroll ' + courses[0].to_string() + ' to ' + s.to_string())
            the_university.enroll_student(s, courses[0])
        else:
            print('cannot find student in course ' + course_name_1)

        courses = the_university.find_course(course_name_2)
        if len(courses) > 0:
            print('enroll ' + s.to_string() + ' in ' + courses[0].to_string())
            the_university.enroll_student(s, courses[0])
        else:
            print('cannot find student with course name ' + course_name_2)
    else:
        print('cannot find student with name', student_to_look_for)

    print('here are the enrollments in the university:')
    the_university.show_enrollments()

    student_id_to_look_for = 101
    s = the_university.find_student_by_id(student_id_to_look_for)
    if s is not None:
        courses = the_university.get_courses(s)
        if len(courses) > 0:
            print('enroll ' + s.to_string() + ' in ' + courses[0].to_string())
        else:
            print('cannot find student with id #', student_id_to_look_for)

    print('here are the enrollments in the university:')
    the_university.show_enrollments()

#--------------------------------------------------

def main():
  my_university = university.University().get()
  simple_runtime_test(my_university)

#--------------------------------------------------

main()