import csv

class CSVParser():

    file = ""
    lines = ""
    namesList = set()

    def openCSV(self, file):
        try:
            self.file = open(file, 'r')
            self.lines = csv.reader(self.file, delimiter=',', quotechar='"')
        except FileNotFoundError:
            print('File cannot be found')
        except FileExistsError:
            print(' File not exists')

    def closeCSV(self):
        self.file.close()

    def findCountByName(self):
        counter = 0
        for line in self.lines:
            if counter != 0:
                self.namesList.add(line[1])
            counter = counter + 1
        count = len(self.namesList)
        message = "This CSV File has total diffrent names: {}".format(count)
        print(message)

csvParser = CSVParser()
csvParser.openCSV('../dummy/csv/dummy.csv')
csvParser.findCountByName()
csvParser.closeCSV()
