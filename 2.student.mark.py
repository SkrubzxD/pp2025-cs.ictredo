#note to use .input() and .list()

''' 
Input functions:
• Input number of students in a class (Done)
• Input student information: id, name, DoB 
• Input number of courses (Done)
• Input course information: id, name 
• Select a course, input marks for student in this course
 Listing functions:
• List courses
• List students
• Show student marks for a given course
Schema :
• StudentID -> studentName, DoB
• CourseID -> courseName, studentMark, studentID
• listStudentMark(CourseID) -> studentMark
'''
studentNameList = []
studentIDList = []
studentDoBList = []
courseIDList = []
courseNameList = []

numberOfStudents = 0
numberOfCourses = 0

def inputnumberOfCourses():
    numberOfCourses = input("Enter number of courses: ")
    return numberOfCourses


class Entity:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def toString(self):
        print(f"Name: {self.name}\n ID: {self.ID}\n")

class Student(Entity):
    super().name
    super().ID
    DoB = ""
    # day, month, year = DoB.split("/")
    def inputStudentInfo(): 
        #init student info
        name = super().input("Enter name: ")
        ID = super().input("Enter ID: ")
        DoB = super().input("Enter DoB: ")
        super().nameList.append(name)
        super().IDList.append(ID)
        super().DoBList.append(DoB)

    def toString(self):
        super().toString()
        print(f"DoB: {self.DoB}\n")

class Course(Entity):
    numberOfStudents = 0
    studentMark = []
    def __init__(self, name, ID):
        super().__init__(name, ID)

    def inputStudentsInClass(self, number):
        numberOfStudents = input("Enter number of students: ")
        return numberOfStudents


def listStudentMarks(class_type = "Course", a = Course):
    for i in a.studentMark:
        print(f"Student: {a.studentMark.index(i)+1}\n Mark: {i}\n")

#main 
Student1 = Student()
Student1.inputStudentInfo()
Student1.toString()

Course1 = Course()
Course1.inputCourseInfo()

# listStudents()
# listCourses()
listStudentMarks(Course = "Course1")