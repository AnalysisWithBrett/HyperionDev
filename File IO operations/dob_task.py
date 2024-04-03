# Opening and reading the file dob.txt
with open("DOB.txt", 'r+') as dob:
    info = dob.readlines() # storing each line from the txt file into a list
    print("\nName") 
    
    for name in info: # iterating through the info list
       name = name.strip() # removing \n
       name = name.split() # separating the string by spaces

       firstName = name[0] # storing the first item from the name list into first name
       lastName = name[1] # storing the second item from the name list into last name

       print(f'{firstName} {lastName}') # printing out the names

    
    print("\nBirthdate")


    for date in info: # iterating through the info list
        date = date.strip() # removing \n
        date = date.split() # separating the string by spaces

        day = date[2] # storing the 3rd item from the date list into day
        month = date[3] # storing the 4th item from the date list into month
        year = date[4] # storing the 5th item from the date list into year

        print(f'{day} {month} {year}') # printing out the birthdate

