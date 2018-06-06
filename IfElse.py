import random

#################################
# Playing with String
print('#'*33)
#################################

'''
    Simple If Else
'''

checked = False

if(checked == True):
    print("Checked")
else:
    print("Not Checked")

#################################
# Playing with String
print('#'*33)
#################################

username = "d8devs"

if(username == "d8devs"):
    print("User {} Logged".format(username))
else:
    print("User not logged, please login")

#################################
# Playing with String
print('#'*33)
#################################

age = 17

if(age < 18):
    print("You are not allowed")
else:
    print("Welcome")

#################################
# Playing with String
print('#'*33)
#################################

age = random.randint(14, 45)
print(age)

if(age >= 14 and age < 18):
    print("Level 1")
if(age >= 18 and age <= 45):
    print("Level 2")

#################################
# Playing with String
print('#'*33)
#################################

'''
    If Else with List
'''
students = ["Ahmet", "Hasan", "Seyma", "Sare"]

if "Sare" in students:
    print("Yes, Ms. Sare is student")

if "Neslisah" not in students:
    print("Yes, Ms. Neslisah isn't student")

#################################
# Playing with String
print('#'*33)
#################################

'''
    elif
'''
currency = "€"
if currency == "₺":
    print("Turkish Lira")
elif currency == "€":
    print("EURO")
elif currency == "$":
    print("U.S. Dollar")
elif currency == "¥":
    print("JAPAN Yen")
