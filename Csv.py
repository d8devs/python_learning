#################################
#Playing with String
print('*'*33)
#################################

'''
    CSV file open, read and create list pro Line
'''

with open('dummy/csv/dummy.csv') as file:
    for line in file:
        print(line.strip().split(";"))

#################################
#Playing with String
print('*'*33)
#################################

'''
    CSV Read and for example : Create Table 
'''
print('-'*53)
print("| CITY\t\tPOPULATION(rounded)\t\tRATING\t\t\t|")
print('-'*53)
with open('dummy/csv/dummy.csv') as file:
    for line in file:
        data = line.strip().split((';'))
        text = "{}\t\t{}\t\t{}".format(data[0], data[1], data[2])
        print(text)
