#################################
# Playing with String
print('*'*33)
#################################

'''
    Create a Student List
'''
students = ["Ahmet", "Hasan", "Seyma", "Sare"]
print(students)

#################################
# Playing with String
print('*'*33)
#################################

'''
    Add Element in to the List
'''
students.append("Neslisah")
print(students)

#################################
# Playing with String
print('*'*33)
#################################

'''
    Count the items of a list 
'''
print(len(students))

#################################
# Playing with String
print('*'*33)
#################################

'''
    Get 3. Element with Elemet Position
    Position Numbers Start 0,1,2...
'''
print(students[2])

#################################
# Playing with String
print('*'*33)
#################################

'''
    Get 1. and 4. Element and write together
'''
print("1. Person : {}, 4. Person: {}".format(students[0], students[3]))

#################################
# Playing with String
print('*'*33)
#################################


'''
    Remove Last Item of a List
'''
print("BEFORE:")
print(students)
print("AFTER:")
removedItem = students.pop()
print(students)
print("REMOVED:")
print(removedItem)
#################################
# Playing with String
print('*'*33)
#################################


'''

    Diffrent Action with List and List elements
'''
#add new list items with plus
students = ["Domonique Brittingham", "Marjorie Ruddy", "Janelle Rodenberger", "Jarvis Flenniken", "Maddie Batchelor", "Priscila Weisgerber", "Zetta Lorenz", "Dorcas Daniel"] + ["Max Mustermann"]

#remove item
students.remove('Max Mustermann')

# get items between 2 and 4
print(students[2:4])

#List Comprehensions
xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [k + k for k in xs]

print(xs)
print(ys)













