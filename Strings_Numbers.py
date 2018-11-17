import random

# int to str
age = random.randint(14,90)
print("Selam !")
print("Age : " + str(age))

# Write String with Format With Multiple Placeholder
gender = "Male"
print("Age : {} ".format(age))
print("Age : {}, Gender : {} ".format(age, gender))

# Find Word Count from Text
text = "Lorem Ipsum damit lamor"
count = len(text.split(" "))
print(count)

# Upper
print(text.upper())

# Lower
print(text.lower())

# If string start with "example characters.."
if text.startswith("L"):
    print("Text start with >> L <<")

# If string end with "example characters.."
if text.endswith("r"):
    print("Text end with >> r <<")

# Remove Characters or Whitespaces
word = "         Hello ..  "
print(word.strip(" ."))

# Remove Characters or Whitespaces at the Left Side
word = "         Hello ..  "
print(word.lstrip(" "))


# Remove Characters or Whitespaces at the Right Side
word = "         Hello ..  "
print(word.rstrip(" "))

# Find Character in the Sentence
print(word.find('e'))

# Replace Character
print(word.replace("e", "a"))


