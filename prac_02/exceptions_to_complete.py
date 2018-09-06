finished = False
result = 0
while not finished:
    try:
        user_value = int(input("please enter an integer"))
        finished = True
        result = user_value
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)