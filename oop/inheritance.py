
class Student():
     def __init__(self, firstname, lastname):
         self.firstname = firstname
         self.lastname = lastname
         self.term = 1

     def name(self):
         return self.firstname + " " + self.lastname

                    #thats mean get all variable and methods from Student
class WorkingStudent(Student):
        # Solution One - Method Override
        '''
        def __init__(self, firstname, lastname, company):
            self.firstname = firstname
            self.lastname = lastname
            self.company = company
        '''

        # Good Solution
        def __init__(self, firstname, lastname, company):
            # super() mean Parent Class
            super().__init__(firstname, lastname)
            self.company = company

        # Method Overriding
        def name(self):
            return super().name() + " (But Working Stundent) Company : " + self.lastname

# Create Class with Inheritance
workingStudent = WorkingStudent("Childkiller", "Camaroon", "Killer CO.")
print(workingStudent.name())



# Create List with Classes

students = [
    WorkingStudent("Childkiller", "Camaroon", "Killer CO."),
    Student("Child", "Killer Camaroon 2"),
    Student("Child", "Killer Camaroon 3"),
    WorkingStudent("Childkiller", "Camaroon 4", "Killer CO.")
]

for student in students:
    print(student.name())