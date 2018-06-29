#################################
# Playing with String
print('_' * 33)
#################################

# new Tupel
tupel = (1, 2, 3)
print(tupel[0])

# update or append? not possible
# because tupel is immutable
# we can only reading values from tupel

# print
print(tupel[2])

'''
    Working with Tupel
'''
student = ("Necmettin Erbakan", 'd8', 'Helper')
name, target, position = student

print(name)
print(target)
print(position)

#################################
# Playing with String
print('_' * 33)
#################################

'''
    with Function
'''
def get_student():
    return ("Koray Zorluoglu", 'd8', '2# Helper')

name, target, position = get_student()

print(name)
print(target)
print(position)

#################################
# Playing with String
print('_' * 33)
#################################
'''
    Tupel List
'''

persons = [
    ("Necmettin Erbakan", 'd8', 'Helper'),
    ("Koray Zorluoglu", 'd8', '2# Helper')
]

for person in persons:
    name, target, position = person
    print(name)
    print(target)
    print(position)
