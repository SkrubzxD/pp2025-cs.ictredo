from course import CourseList, Course
from student import StudentList, Student
import curses


'''
Practical work 4: modularization
• Decorate your UI with curses module 
• Split your program 3.student.mark.oop.math.py to modules
and packages in a new pw4 directory [Done]
• input.py: module for input 
• output.py: module for curses output 
• domains: package for classes  
• main.py: main script for coordination [Done]
'''

stdscr = curses.initscr()


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

