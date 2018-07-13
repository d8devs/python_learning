import csv

with open("../dummy/csv/dummy.csv", newline='') as file:
    csv_file = csv.reader(file, delimiter=',', quotechar='"')
    for line in csv_file:
        print(line)