"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# EmployeeSales = float(input("Sales in dollars ($): "))
# if EmployeeSales >= 1000:
#     BonusCalculated = EmployeeSales * 0.15
#     print("Your bonus is: $",BonusCalculated)
# elif EmployeeSales < 1000:
#     BonusCalculated = EmployeeSales * 0.10
#     print("Your bonus is: $",BonusCalculated)

"""naggy version"""
EmployeeSales = float(input("please enter Sales in dollars ($): "))
while EmployeeSales > 0:
    if EmployeeSales >= 1000:
        BonusCalculated = EmployeeSales * 0.15
        print("Your bonus is: $", BonusCalculated)
    elif EmployeeSales < 1000:
        BonusCalculated = EmployeeSales * 0.10
        print("Your bonus is: $", BonusCalculated)
    EmployeeSales = float(input("please enter Sales in dollars ($): "))


