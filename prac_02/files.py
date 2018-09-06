# OUTPUT_FILE = "data.txt"
# outfile = open(OUTPUT_FILE, 'w')
# username = str(input("Please enter your name"))
# print(username, file=outfile)
# outfile.close()

# IN_FILE = "data.txt"
# inputfile = open(IN_FILE, 'r')
# username = inputfile.read().strip()
# print("name:", username)
# inputfile.close()

IN_FILE = "numbers.txt"
inputfile = open(IN_FILE, 'r')
num1 = int(inputfile.readline())
num2 = int(inputfile.readline())
total = num1 + num2
print("total", total)
inputfile.close()
