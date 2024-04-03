# Asking the user for the number of students registering
students = int(input("How many students are registering? "))

# Creating an empty list to store student ID
register = []


# Iterates through the number of students you have given and asks you their student ID
for i in range(students): 
    id = input("What is the student number? ")
    register.append(f'{id}..............') # adds student ID to the list

# Writes the student ID to the text file with new lines added
with open("reg_form.txt", 'w+') as form:
    form.write("\n".join(register))




