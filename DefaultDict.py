from collections import  defaultdict

# Example Constructor Method for defaultdict
def generate():
    print("generate() work")
    return 0
d = defaultdict(generate)

# If this key not exist, this can't be problem,
# defaultdict use generate method and write 0
print(d["notExist"])

# Print d dict
print(d)
# And can be updated
d["notExist"] = d["notExist"] + 5
# Print d dict
print(d)

# This int constructor write 0 as value for key
p = defaultdict(int)
words = ["Selam", "Hallo", "Hello"]

for word in words:
    p[word] = p[word] + 1

print(p)