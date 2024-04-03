# Asking the user
str_manip = input("Please give me a word/sentence: ")

# Printing the length of the word provided by the user
print("This is the length of your word/sentence: " + str(len(str_manip)))

# Finding the last letter of the word/sentence
last_letter = (str_manip[-1:])
print("This is the last letter: " + last_letter)

# Replacing last letter and other letters similar to it with @
replacement = str_manip.replace(last_letter, '@')
print("Letter replaced with @: " + replacement)

# Printing the last 3 letters backwards
print("Last 3 letters backwards: " + str_manip[:-4:-1])

# First three characters
firstThree = str_manip[:3]

# Last two characters
lastTwo = str_manip[-2::]

# First three characters joined with last to characters
joinedWord = firstThree + lastTwo
print(joinedWord)