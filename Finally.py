try:
    file = open('dummy/txt/dummy.txt', 'r')
    print(file)
    print(5 / 0)
    file.close()
except FileNotFoundError:
    print("Datei wurde nicht gefunden")
#except ZeroDivisionError:
 # print("This not allowed divide by zero")
 # file.close()
finally:
    print("Finaly Operation")
    file.close()