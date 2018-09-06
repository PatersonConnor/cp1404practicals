import os

print("The files and folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)

# MIN_LENGTH = 3
# password = input("Please enter a password: ")
#
# while len(password) < MIN_LENGTH:
#     print("Password too short!")
#     password = input("Please enter a password: ")
#
# for i in password:
#     print("*")