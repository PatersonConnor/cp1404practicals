item_count = int(input("Number of items: "))
item_prices = []
while item_count < 1:
    print("Invalid number of items!")
    item_count = int(input("Number of items: "))
for i in range(0, item_count):
    single_cost = float(input("Price of item:"))
    item_prices.append(single_cost)

print("total price for {} items is: ${:.2f}".format(item_count, sum(item_prices)))
#TODO Figure out how to get the total value without a list!


# for i in range(0, starCount + 1):
#     print("*" * i)
# print()
