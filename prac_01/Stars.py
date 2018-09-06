# print n stars. Ask the user for a number, then print that many stars (*), all on one line

# starCount = int(input("please enter the amount of Stars you wish to be printed."))
# for i in range (0, starCount):
#     print("*", end="")


starCount = int(input("please enter the amount of Stars you wish to be printed."))
for i in range (1, starCount + 1):
    print("*" * i)
print()
