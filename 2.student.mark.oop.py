# Class student with Encapsulation
class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def get_ID(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    def set_ID(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name
    
    def set_dob(self, dob):
        self.__dob = dob

# Class course with Encapsulation
class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_ID(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name

# Class mark for student
class Mark: 
    def __init__(self, course, student, mark):
        self.__course = course
        self.__student = student
        self.__mark = mark
    
    def get_mark(self):
        return self.__mark
    
    def get_student(self):
        return self.__student
    
    def get_course(self):
        return self.__course    

# Action class 
class University:
    def __init__(self):
        self.__num_student = 0
        self.__num_course = 0
        self.__student = []
        self.__course = []
        self.__mark = []

    def get_num_student(self):
        return self.__num_student
    
    def get_num_course(self):
        return self.__num_course
    
    def get_student(self):
        return self.__student
    
    def get_course(self):
        return self.__course
    
    def set_student(self):
        self.__num_student = input("Enter the number of student: ")
        for i in range(self.__num_student):
            id = input(f"Enter Student {i+1} ID: ")
            name = input(f"Enter Student {i+1} name: ")
            dob = input(f"Enter Student {i+1} Date of Birth: ")
            student_info = Student(id, name, dob)
            self.__student.append(student_info)

    def set_course(self):
        self.__num_course = input("Enter the number of course: ")
        for i in range(self.__num_course):
            id = input(f"Enter Course {i+1} ID: ")
            name = input(f"Enter Course {i+1} name: ")
            course_info = Student(id, name)
            self.__course.append(course_info)

    def set_mark(self):
        course_order = input("Input course ID to put mark: ")
        for student in self.__student:
            mark = float(input(f"Input score for {Student.get_name()} in {course_order}: "))
            student_mark = Mark(course_order, student, mark)
            self.__mark.append(student_mark)

    def list_student(self):
        print("- List of students in class: ")
        for i in enumerate(self.__student):
            print(f"{i+1}. \n- Student ID: {Student.get_ID} \n- Student Name: {Student.get_name} \n- Student DoB: {Student.get_dob}")
        
    def list_course(self):
        print("- List of courses in class: ")
        for i in enumerate(self.__course):
            print(f"{i+1}. \n- Course ID: {Course.get_ID} \n- Course Name: {Course.get_name}")

    def list_mark(self, course_name):
        print("- List of students in class: ")
        for i in enumerate(self.__student):
            print(f"{i+1}. \n- Student ID: {Student.get_ID} \n- Student Name: {Student.get_name} \n- Student DoB: {Student.get_dob}")
        
        print("- List of courses in class: ")
        for i in enumerate(self.__course):
            print(f"{i+1}. \n- Course ID: {Course.get_ID} \n- Course Name: {Course.get_name}")

        for course in self.__course: 
            if Course.get_name() == course_name:
                print(f"\nList scores of students in {Course.get_name()}: \n")
                for mark in self.__mark:
                    if Mark.get_course() == course_name:
                        print(f"{Mark.get_student().get_name()}: {Mark.get_score()}")
                    else:
                        print(f"\nCourse {course_name} not found.")


# print("- Information of student: ")
# University.set_student()

# print("- Information of course: ")
# University.set_mark()

Short = University()

while True: 
        print("====================================================================================")
        print("Select option: ")
        print("1: Input mark for student")
        print("2: Show Students List")
        print("3: Show Courses List")
        print("4: Show Student's marks List") 
        # print("5: Add Student") 
        # print("6: Add Course") 
        # print("7: Remove Student") 
        # print("8: Remove Course") 
        print("9: Do nothing :D")
        option = input("Enter the option: ")
        print("====================================================================================")
        if option == '1': 
            Short.set_student()
        elif option == '2': 
            Short.list_student()
        elif option == '3': 
            Short.list_course()
        elif option == '4': 
            Short.list_mark()
        # elif option == '5': 
            
        # elif option == '6':
            
        # elif option == '7':
            
        # elif option == '8':
            
        elif option == '9':
            break
        else:
            option = (input("Please enter again: "))
