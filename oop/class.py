#################################
#Playing with String
print('*'*33)
#################################

'''
    Create Class
'''
class Teacher():
    pass


# Create a Teacher using Teacher Class
erbakan = Teacher()
erbakan.name = "Necmettin"
erbakan.lastname = "Erbakan"

# Create a another Teacher with same Teacher Class
karamollaoglu = Teacher()
karamollaoglu.name = "Temel"
karamollaoglu.lastname = "Karamollaoglu"

print(erbakan.name)
print(erbakan.lastname)
print(karamollaoglu.name)
print(karamollaoglu.lastname)


'''
    Create Class with Constructor and Methods
'''

class Student():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def getFullname(self):
        print(self.name + "" + self.lastname)

# Create a Student using Constructor
koray = Student("d8", "devs")
# run Class method
koray.getFullname()



'''
    Create Class and Methods for Example
'''

class Student():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        # set standart variable with value
        self.term = 1

    def getFullname(self):
        # add term variable
        print(self.name + "" + self.lastname + "(Semester " + str(self.term) + ")")

    def increase_term(self):
        self.term = self.term + 1

# Create a Student
koray = Student("d8", "devs")
# run Class method
koray.getFullname()
# update this student semester with good solution/oop best practice way
koray.increase_term()
koray.getFullname()