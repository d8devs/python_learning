#################################
#Playing with String
print('#'*33)
#################################

dict = {
    "Kudüs": "KDS",
    "Istanbul" : "IST",
    "Sam" : "SAM"
}

# Get values basic example
for key in dict:
    value = dict[key]
    message = "Key {} : Value : {}".format(key, value)
    print(message)

#################################
#Playing with String
print('*'*33)
#################################


# Get with Tuppel Method with items function from Dictionary
for key, value in dict.items():
    message = "Key {} : Value : {}".format(key, value)
    print(message)
    #or
    print(key + ": " + value)