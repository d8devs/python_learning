#################################
#Playing with String
print('*'*33)
#################################

'''
    File Open and read line by line
'''
file = open("Example.txt", "r")
for line in file:
    # strip remove the new line string from line "\n"
    print(line.strip())
    print("--")

for line in file:
    #with "\n"
    print(line)
    print("--")

#################################
#Playing with String
print('*'*33)
#################################

'''
    File open and write
'''

writeFile = open("Example.txt", "w")

writeFile.write("Sed efficitur sagittis elit, sit amet scelerisque lectus fringilla eget.\n ")
writeFile.write("Interdum et malesuada fames ac ante ipsum primis in faucibus.\n")
writeFile.write("Maecenas non ex commodo, suscipit lorem id, finibus tortor.\n")
writeFile.write("Phasellus nec nunc eget sem blandit faucibus. Pellentesque consectetur lacus in dui consectetur efficitur.\n")
writeFile.write("Aliquam scelerisque dictum nunc id euismod.\n")
writeFile.write("Nunc justo justo, convallis sed elit sit amet, aliquet vehicula sapien.\n")

writeFile.close()

#################################
#Playing with String
print('*'*33)
#################################

'''
    File open and Append
'''
getFile = open("Example.txt", "a")
getFile.write("ADD THIS LINE AFTER THE END OF FILE")
getFile.close()

#################################
#Playing with String
print('*'*33)
#################################

'''
    Close Automatic File if any error has
'''

with open('Example.txt', 'r') as file:
    for line in file:
        # This function not created, that >>>with<<< tag from  >>>with open("Example"...<<< mean close file if this action error has
        makeSomething()
        print(line)

#################################
#Playing with String
print('*'*33)
#################################

'''
    File Close    
'''

openFile = open("Example.txt", "r")
# WORK IS HERE or something
openFile.close()
