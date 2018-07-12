'''
    Create Class without Capsuling
'''

class PhoneBook():

    def __init__(self):
        self.entries = {}

    def add(self, name, phone_number):
        self.entries[name] = phone_number



book = PhoneBook()
book.add("Necmettin Erbakan", "+9033333333")
book.add("Temel Karamollaoglu", "+9033336666")

print(book.entries)


'''
    Create Class with Capsuling
'''
class PhoneBook():

    def __init__(self):
        self.__entries = {}

    def add(self, name, phone_number):
        self.__entries[name] = phone_number

    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None

book = PhoneBook()
book.add("Necmettin Erbakan", "+9033333333")
book.add("Temel Karamollaoglu", "+9033336666")

# print(book.entries)
print(book.get("Necmettin Erbakan"))




'''
    Class with Magic Methods
'''

class PhoneBook():

    def __init__(self):
        self.entries = {}

    def add(self, name, phone_number):
        pass

    def get(self, name):
        pass

    # Magic Methods
    def __str__(self):
        return "STR: PhoneBook ( Total Entries : " + str(len(self.entries))+ ")"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.entries)



book = PhoneBook()

print(book)
print(len(book))


