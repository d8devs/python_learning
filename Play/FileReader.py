

class FileReader():
    def __init__(self, filename):
        self.filename = filename

    def lines(self):
        lines = []
        with open(self.filename, '+r') as file:
            for line in file:
                lines.append(line.strip())
        return lines


class CSVReader(FileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def lines(self):
        lines = []
        for line in super().lines():
            line = line.split(",")
            lines.append(line)
        return lines


fileReader = FileReader("../dummy/txt/dummy.txt")
print(fileReader.lines())

csvReader = CSVReader("../dummy/csv/dummy.csv")
print(csvReader.lines())