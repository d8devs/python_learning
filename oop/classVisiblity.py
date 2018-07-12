#################################
#Playing with String
print('-'*33)
#################################


'''
    Create Class and Checking increase method before Update 
'''
class Student():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        # set standart variable with value
        self.term = 1

    def getInformation(self):
        # add term variable
        print(self.name + "" + self.lastname + "(Semester " + str(self.term) + ")")

    def increase_term(self):
        # here is update
        # that mean, if bigger then 3, pass this function
        if(self.term >= 3):
            return
        self.term = self.term + 1


# We heave new Student created and updated him semester's and
# everyting is good.
d8devs = Student("D8", "Devs")
d8devs.increase_term()
d8devs.increase_term()
d8devs.increase_term()
d8devs.getInformation()
# But, What going on if I this variable manually updating
d8devs.term = 1000000
d8devs.getInformation()
# How to Fix? Answer : Visibilty

'''
    Create Class and Variables with  Private Visibilty
'''
class Student():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        # here is private visibility tag
        # this two underline " __ " meaning this variable is private
        # only this variable value updateing under this Class functions
        self.__term = 1

    def getInformation(self):
        # add term variable
        print(self.name + "" + self.lastname + "(Semester " + str(self.__term) + ")")

    def increase_term(self):
        # now we updating under any Class Function
        if(self.__term >= 3):
            return
        self.__term = self.__term + 1

    def getTerm(self):
        return  self.__term

# We heave new Student created and updated him semester's and
# everyting is good.
d8devs = Student("D8", "Devs")
d8devs.increase_term()
d8devs.increase_term()
d8devs.increase_term()
d8devs.getInformation()
# But, What going on if I this variable manually updating
# Answer: Nothing.
d8devs.term = 1000000
d8devs.getInformation()
# we have fixed this wrong/manually update, with getTerm function we can reading value from private Variable
print(d8devs.getTerm())



'''
    Create Class and Methods with Private Visibility
'''
class Student():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        # here is private Method for default value writing.
        self.__setTerm()

    def getInformation(self):
        # add term variable
        print(self.name + "" + self.lastname + "(Semester " + str(self.__term) + ")")

    def increase_term(self):
        if(self.__term >= 3):
            return
        self.__term = self.__term + 1

    def getTerm(self):
        return  self.__term

    # here is our private method
    def __setTerm(self):
        self.__term = 1


# Create Student
d8devs = Student("D8", "Devs")
d8devs.getInformation()
'''
but setTerm method not visible outside from Class. Remove "#" Comment from line, if you this testing!
'''
#d8devs.__setTerm()
''' 
    d8devs.__setTerm()
D8Devs(Semester 1)
AttributeError: 'Student' object has no attribute '__setTerm'
'''


