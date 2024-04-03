# Creating a variable containing *
asterisk = "*"

# Creating a single loop
for number in range(1, 10):
    if number < 6:
        print(number * asterisk) # prints out the asterisks within the range 1 - 5
    else:
        print((10 - number) * asterisk) # 10 is deducted by the following numbers beyond 5 multiplied the *

