# Asking user to input three integers
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
num3 = int(input("Please enter one more number: "))

# Calculating the sum of the numbers
sumNumbers = num1 + num2 + num3
print("Sum of all numbers: " + str(sumNumbers))

# Calculating the difference between first and second number
diffNumbers = num1 - num2
print("Difference between first and second number: " + str(diffNumbers))

# Multiplying the third number with the first
multiNumbers = num3 * num1
print("Third number multiplied with first number: " + str(multiNumbers))

# Calculating the sum of all numbers and divide it by the third number
divNumbers = (num1 + num2 + num3) / num3
print("Sum of all numbers and divide it by the third number: " + str(divNumbers))