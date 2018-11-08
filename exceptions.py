
# x = 0
# print(5 / x)
# here coming ZeroDivisionError Error
# print(5)


# with open("date.xyz", "r") as file:
    # print(file)
    # here coming FileNotFoundError


try:
    print(5 / 0)
except ZeroDivisionError:
    print("not allowed to divide by zero.")

try:
    with open('date.xyz', 'r') as file:
        print(file)
except FileNotFoundError:
    print("This file can't be found")
print(5)



try:
    print(5 / 0)
    with open('date.xyz', 'r') as file:
        print(file)
except ZeroDivisionError:
    print("Not allowed to divide by zero")
except FileNotFoundError:
    print("This file cannot be found")


def do_something():
    print(5/0)

try:
    do_something()
except ZeroDivisionError:
    print("Not Allowed to divide by zero")

class InvalidEmailError(Exception):
    pass

def send_mail(email, subject, content):
    if not "@" in email:
        raise InvalidEmailError("Email doest not contain an @")


try:
    send_mail('tet','test','test')
except InvalidEmailError:
    print("Please fill this Input With Real E-mail Address")
