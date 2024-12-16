#note to use .input() and .list()
import math
from datetime import datetime
import numpy as np
''' 
Copy your practical work 2 to 3.student.mark.oop.math.py [Done]
• Use math module to round-down student scores to 1-digit decimal upon input, floor() [Done]
• Use numpy module and its array to 
1. Add function to calculate average GPA for a given student 
2. Weighted sum of credits and marks 
• Sort student list by GPA descending [Done]

Schema :
studentGPAList = []
- studentGPA = for studentMark in coursesParticipated : totalGPA += studentMark
- GPA = totalGPA / len(coursesParticipated)
studentGPAList[::-1].sort() 
'''

'''
Practical work 4: modularization
• Decorate your UI with curses module 
• Split your program 3.student.mark.oop.math.py to modules
and packages in a new pw4 directory
• input.py: module for input    
    • output.py: module for curses output   
    • domains: package for classes  
• main.py: main script for coordination 
'''
courseList = []
studentList = []
class StudentList:
    studentNameList = []
    studentIDList = []
    studentDoBList = []
    studentGPAList = []
    numberOfStudents = 0

class CourseList:
    courseIDList = []
    courseNameList = []
    numberOfCourses = 0

class Entity:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def toString(self):
        print(f"Name: {self.name}\n ID: {self.ID}")

class Student(Entity):



    def calculateGPA(self):
        for i in courseList : 
            totalGPA += courseList[i].studentID[i]
        return round(totalGPA / (courseList.index()+1) ,2)
    studentGPA = calculateGPA()
    def __init__(self, name, ID, DoB):
        super().__init__(name, ID)
        self.DoB = datetime.strptime(DoB, '%d/%m/%Y')
        studentList.append(self)
    # day, month, year = DoB.split("/")

    # def inputStudentInfo(): 
    #     name = super().input("Enter name: ")
    #     ID = super().input("Enter ID: ")
    #     DoB = super().input("Enter DoB: ")
    #     super().nameList.append(name)
    #     super().IDList.append(ID)
    #     super().DoBList.append(DoB)

    def toString(self):
        super().toString()
        print(f"DoB: {self.DoB}\n")


    

class Course(Entity):
    numberOfStudents = 0
    studentMark = []
    studentList = []
    def __init__(self, name, ID):
        super().__init__(name, ID)
        courseList.append(self)

    def inputStudentIntoCourse(self, a = Student):
        self.studentList.append(a)
        return self.studentList
    
    def inputStudentMark(self, a = Student, mark = float):
        if a in self.studentList:
            self.studentMark.append(round(mark,2))
        else:
            print(f"{a.ID} doesn't exist in course!")

    def sortByGPA(self):
        self.studentMark[::-1].sort()


    def listStudentMarks(self):
        for i in range (0, len(self.studentList)):
            print(f"Student: {self.studentList[i].name}\n Mark: {self.studentMark[i]}\n")

class Menu():
    options = 0
    def __init__(self, optionCardinality):
        self.options = optionCardinality
    def display(self):
        for i in range (1, self.options):
            print(f"{i}. option")





#main 
def MainMenu():
    print('''
    Welcome to Student Management Simulator

    This build has the following function:
    Test
    ''')
    Test()
def Test():
    Student1 = Student("Andy", "23BI14000", "01/01/2000")
    Student1.toString()
    Course1 = Course("Math", "M001.1")
    Course1.inputStudentIntoCourse(Student1)
    Course1.inputStudentMark(Student1, 13.3333)
    Course1.listStudentMarks()
MainMenu()
# listStudents()
# listCourses()