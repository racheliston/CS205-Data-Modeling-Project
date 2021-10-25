import university
import student
import course

# exercise code by calling functions to ensure code is being developed correctly
# and we are testing correct functions

def simple_runtime_test(theUniversity):
    print("Simple Runtime Test")


def main():
  myUniversity = university.University().get()

  simple_runtime_test(myUniversity)


main()
