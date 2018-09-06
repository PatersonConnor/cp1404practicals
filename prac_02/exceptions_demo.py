try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")#when the user enters a non-numerical value
except ZeroDivisionError:
    print("Cannot divide by zero!") #Occurs when dividing by zero. Yes, you could change it to print 0 as a default, or keep asking for a valid value in a loop
print("Finished.")