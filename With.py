
# This way would be file closed.
file = open('dummy/txt/dummy.txt', 'r')
print(file)
file.close()

# otherwise with "with" option, it opens the file first and after that it closes.
def something():
    with open('dummy/txt/dummy.txt', 'r') as file:
        print(file)
        return True

something()