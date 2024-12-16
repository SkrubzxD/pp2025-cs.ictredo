'''
Make a new Python program
• Name it «1.student.mark.py»
• Use tuples, dicts, lists, NO objects/classes
• Build a student mark management system
Input functions:
• Input number of students in a class
• Input student information: id, name, DoB
• Input number of courses
• Input course information: id, name
• Select a course, input marks for student in this course
 Listing functions:
• List courses
• List students
• Show student marks for a given course
'''

studentID = []
studentName = []
courseID = []
studentMark = []
courseName = []
studentDoB = []

#def inputStudentNumberInClass(int ID): 

def inputStudentInfo():
    ID = input("ID: ")
    name = input("Name: ")
    DoB = input("DoB: ")
    studentID.append(ID)
    studentName.append(name)
    studentDoB.append(DoB)
    Menu()


#def inputCourseNumber(int num):
#def inputCourseInfo(id, name) :
#def inputStudentMarkToCourse(int courseID):

def listCourses():
    print ("Courses: \n")

    for i in courseID:
        print(courseName[i])
    Menu()

def listStudents():
    print("\n   Students: \n")
    for i in studentID:
        print(studentID.index(i)+1, ":", i)
    Menu()
#def listStudentMarks(int courseID):

# Menu
menu = '''
===
Select option
1. Input Student Info
2.
3. list students
4. list courses
5. Exit
===
'''
def Menu():
    print(menu)
    option = int(input("Enter number: "))
    match option:
        case 1: 
            inputStudentInfo()
        case 3:
            listStudents()
        case 4: 
            listCourses()
        case 5:
            exit()
        case default:
            Menu()
    
#main
Menu()
