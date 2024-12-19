import Entity
import CourseList

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