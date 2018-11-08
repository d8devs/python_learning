# List
list = ['List Element 1', 'List Element 2']
# Dictionary
dictionary = { 'variable' : 'wert', 'message' : 'Selam' }

# Set with List
s = ['Hallo', 'Mars']
# add this World everytime at the Last Element
s.append('World')
print(s)

# Set with Dictionary
s = {"Hallo", "Mars"}
# add this World everytime as the First Element
s.add('World')
print(s)

# Set same key in to Dictionary is not possible!
s.add('Mars')
print(s)

# Simple tactics
# find only Different Words from Text
text = "Hello World Hello Mars Hello Jupiter"
onlyDifferentWords = set()

for word in text.split(" "):
    onlyDifferentWords.add(word)

print(onlyDifferentWords)

