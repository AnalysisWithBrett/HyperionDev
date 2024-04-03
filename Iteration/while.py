# Create an empty list for the user to input the numbers
num_list = []

# This loop asks the user to ask for input continually until the user enters -1
while True:
    number = int(input("Please enter a number (Type -1 to stop): ")) # user inputs a number multiple times until -1 is used to stop
    if number != -1:
        num_list.append(number) # this line adds the input into the list
        print(f"Number is added to list {num_list}") # shows the list to the user to keep track
        print("") # Creating a space to make the output clean
    else:
        print("You have typed -1. Here is the calculation for the average:") # informs the user that their input is not needed anymore
        print("") # Creating a space to make the output clean
        break

# Calculation for the average
numerator = sum(num_list) # Adds all the numbers in the list
denominator = len(num_list) # Counts the numbers in the list
average = numerator/denominator # Dividing the sum of the numbers by the count of numbers in the list

# Showing the results
print(f'{numerator} / {denominator} = {float(round(average, 2))}') # Prints out the average with the nearest 2 decimal places

