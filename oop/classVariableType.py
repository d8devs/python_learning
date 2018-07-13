
class Student():
     def __init__(self, firstname, lastname):
         self.firstname = firstname
         self.lastname = lastname
         self.term = 1

     def name(self):
         return self.firstname + " " + self.lastname

class WorkingStudent(Student):


        # Good Solution
        def __init__(self, firstname, lastname, company):
            # super() mean Parent Class
            super().__init__(firstname, lastname)
            self.company = company

        # Method Overriding
        def name(self):
            return super().name() + " (Company : " + self.lastname + ")"


workingStudent = WorkingStudent("Children", "Killer Camaroon", "Killer CO.")
normalStudent = Student("Children", "Killer Camaroon Army")

print(type(workingStudent))
print(type(normalStudent))

if type(workingStudent) == Student:
    print("This student created with Student Class")
else:
    print("THis student created with Another Class")

if type(normalStudent) == Student:
    print("This student created with Student Class")

if isinstance(workingStudent, Student):
    print("True")

if isinstance(workingStudent, WorkingStudent):
    print("True")

if isinstance(normalStudent, Student):
    print("True")

if isinstance(normalStudent, WorkingStudent):
    print("True")
else:
    print("False")