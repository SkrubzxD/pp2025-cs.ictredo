import Entity
import CourseList

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
