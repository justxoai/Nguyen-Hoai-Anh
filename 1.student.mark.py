# Input number of student
def input_num_of_student():
    while(1):
        try: 
            num_of_student = int(input("=> Enter the number of students in the class: "))
            if num_of_student <= 0 :
                num_of_student = int(input("=> Please enter again: "))
            else:
                break
        except ValueError:
            print("Number of students in the class must be an integer. Please enter again.")
    return num_of_student

# Input number of course
def input_num_of_course():
    while(1):
        try: 
            num_of_course = int(input("=> Enter the number of courses in the class: "))
            if num_of_course <= 0 :
                num_of_course = int(input("=> Please enter again: "))
            else:
                break
        except ValueError:
            print("Number of course must be an integer. Please enter again.")
    return num_of_course

# Input the information of the student
def input_student(num_of_student):
    Student = []
    for i in range (num_of_student):
        print(f"=> Input information of student number {i+1}:")
        student_ID = input(f"Student {i+1} ID: ")
        student_Name = input(f"Student {i+1} Name: ")
        student_DoB = input(f"Student {i+1} DoB: ")
        student_info = {"id: ": student_ID, "name: ":  student_Name, "dob: ": student_DoB}
        Student.append(student_info)
    return Student

# Input the information of the course
def input_course(num_of_course):
    Course = []
    for i in range (num_of_course):
        print(f"=> Input information of the course {i+1}:")
        course_ID = input(f"Course {i+1} ID: ")
        course_Name = input(f"Course {i+1} Name: ")
        course_info = {"id: ": course_ID, "name: ": course_Name}
        Course.append(course_info)
    return Course

# Input the mark of course for the student
def input_mark_for_student(List_student, List_course):

    print("- List of Student: ")
    for i, student in enumerate(List_student):
        print(f"{i+1}. {student['name: ']} ({student['id: ']})")
    print("====================================================================================")

    print("- List of Course: ")
    for i, course in enumerate(List_course):
        print(f"{i+1}. {course['name: ']} ({course['id: ']})")
    print("====================================================================================")

   
    course_select = int(input("=> Enter the order of the course to put mark for student: ")) - 1  
            
    student_select = int(input("=> Enter the order of the student: ")) - 1   
            
    print(f"- For student name: {List_student[student_select]['name: ']} of the course: {List_course[course_select]['name: ']}")          
    mark = float(input("=> Enter the mark of student of the course: "))
    List_student[student_select].setdefault("course: ", {}).update({List_course[course_select]['name: '] : mark})

# Show list of Students
def list_of_student(List_student):
    print("- List of student in the class: ")
    for i, student in enumerate(List_student):
        print(f"Student {i+1}: \n-Student ID: {student['id: ']} \n-Student Name: {student['name: ']} \n-Student DoB: {student['dob: ']}\n")
        
# Show list of Courses
def list_of_course(List_course):
    print("List of Course: ")
    for i, course in enumerate(List_course):
        print(f"Course {i+1}: \n-Course ID: {course['id: ']} \n-Course Name: {course['name: ']}\n")

# Show mark of the course of student
def show_mark_of_student(List_student):
    print("- List of student in the class: ")
    for i, student in enumerate(List_student):
        print(f"{i+1}) Student {i+1}: \n-Student ID: {student['id: ']} \n-Student Name: {student['name: ']} \n")

    student_select = int(input("=> Enter the student to show the mark for: ")) - 1   
    print("====================================================================================")

    if "course: " in List_student[student_select]:
        print(f"-Student ID: {List_student[student_select]['id: ']} \n-Student Name: {List_student[student_select]['name: ']} \n-Student Marks: {List_student[student_select]['course: ']}\n")
    else: 
        print(f"-Student ID: {List_student[student_select]['id: ']} \n-Student Name: {List_student[student_select]['name: ']} \n-Student Marks: (emtpy)\n")

# Add more Student
def add_student(List_student):
        print(f"=> Input information of student:")
        student_ID = input(f"Student ID: ")
        student_Name = input(f"Student Name: ")
        student_DoB = input(f"Student DoB: ")
        student_info = {"id: ": student_ID, "name: ":  student_Name, "dob: ": student_DoB}
        List_student.append(student_info)

# Add more Course
def add_course(List_course):
    print(f"=> Input information of the course:")
    course_ID = input(f"Course ID: ")
    course_Name = input(f"Course Name: ")
    course_info = {"id: ": course_ID, "name: ": course_Name}
    List_course.append(course_info)

# Remove Student
def remove_student(List_student):
    list_of_student(List_student)

    student_select = int(input("=> Enter the order of student to remove: ")) - 1   
    print("====================================================================================")

    student_info = {"id: ": List_student[student_select]['id: '], "name: ":  List_student[student_select]['name: '], "dob: ": List_student[student_select]['dob: ']}
    List_student.remove(student_info)
    list_of_student(List_student)


# Remove Course
def remove_course(List_course):
    list_of_course(List_course)

    course_select = int(input("=> Enter the order of the course to remove: ")) - 1  
    print("====================================================================================")

    course_info = {"id: ": List_course[course_select]['id: '], "name: ":  List_course[course_select]['name: ']}
    List_course.remove(course_info)
    list_of_course(List_course)

# Main
nos = input_num_of_student()
List_student = input_student(nos)

noc = input_num_of_course()
List_course = input_course(noc)

while True: 
        print("====================================================================================")
        print("Select option: ")
        print("1: Input mark for student")
        print("2: Show Students List")
        print("3: Show Courses List")
        print("4: Show Student's marks List") 
        print("5: Add Student") 
        print("6: Add Course") 
        print("7: Remove Student") 
        print("8: Remove Course") 
        print("9: Do nothing :D")
        option = input("Enter the option: ")
        print("====================================================================================")
        if option == '1': 
            input_mark_for_student(List_student, List_course)
        elif option == '2': 
            list_of_student(List_student)
        elif option == '3': 
            list_of_course(List_course)
        elif option == '4': 
            show_mark_of_student(List_student)
        elif option == '5': 
            add_student(List_student)
        elif option == '6':
            add_course(List_course)
        elif option == '7':
            remove_student(List_student)
        elif option == '8':
            remove_course(List_course)
        elif option == '9':
            break
        else:
            option = int(input("Please enter again: "))
