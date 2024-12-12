#note to use .input() and .list()

''' 
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
Schema :
• StudentID -> studentName, DoB
• CourseID -> courseName, studentMark, studentID
• getMark(StudentID, CourseID) -> studentMark
'''
class Entity():
    name = []
    ID = []
    def list():
        pass
    def input():
        pass
class Student(Entity):
    super().name
    super().ID
    DoB = []
    # day, month, year = DoB.split("/")
    
    def list():
        super().list()


class Course(Entity):
    numberOfStudent = 0
    studentMark = []
    super().name
    super().ID
    #def listStudentMarks():
    #def studentNumber
