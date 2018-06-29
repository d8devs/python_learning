#################################
#Playing with String
print('*'*33)
#################################

'''
    Create  Dictionary 
'''
firstDict = {"Berlin": "BER", "Istanbul": "IST"}

#read
print(firstDict["Istanbul"])
#or
'''
What is diffrence?
if yo with .get reading, python give Value, if not exists then "None"
otherwise direct with dictionary['variable'], python give Value, if not exists then "Traceback Error" then stop python script.
'''
firstDict.get("Istanbul")



#write
firstDict["Kudus"] = "KDS"
print(firstDict)

#check if exists
if "KDS" in firstDict:
    print("KDS is exists")

