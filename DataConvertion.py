#################################
#Playing with String
print('*'*33)
#################################

'''
    str to int
'''
numberOne = "33"
numberTwo = "66"

print(int(numberOne) + int(numberTwo))

#################################
#Playing with String
print('*'*33)
#################################

'''
    str to float
'''
numberOne = "33.33"
numberTwo = "66.66"

print(float(numberOne) + float(numberTwo))

#################################
#Playing with String
print('*'*33)
#################################

'''
    int to str
'''

age = 33
print("Age :" + str(33))

#################################
#Playing with String
print('*'*33)
#################################

'''
    List to str
'''
students = ["Ahmet", "Hasan", "Seyma", "Sare"]
print(", ".join(students))

students_as_string = ", ".join(students)
print(students_as_string)

#################################
#Playing with String
print('*'*33)
#################################

'''
    str to List
'''
stringToList = "Ahmet, Hasan, Seyma, Sare"
list = stringToList.split(", ")
print(list)
