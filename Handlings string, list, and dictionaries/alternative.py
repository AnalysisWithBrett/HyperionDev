# Asking you to write a sentence
string = input("Please enter a sentence: ")

# Empty list used to store letters from your sentence
characters = []

# Iterates through your sentence and store each letter into the list
for letters in (string):
    characters.append(letters)

# iterates through the list and measures the length to each characters
for i in range(len(characters)):
    if i % 2 == 0: 
        characters[i] = characters[i].upper() # letters with indexes that have even numbers are uppercased
    else:
        characters[i] = characters[i].lower() # letters with indexes that have odd numbers are lowercased

# Outputs the list of characters into a sentence with alternating upper and lowercased characters
print("".join(characters))

# Splitting your sentences into a list of words
word = string.split(" ")

# Iterating through the list of words and measures the length of indexed words from 0
for j in range(len(word)):
    if j % 2 == 0:
        word[j] = word[j].upper() # words with even index numbers are uppercased
    else:
        word[j] = word[j].lower() # words with odd index numbers are lowercased

# Outputs the words into a sentence with alternating upper and lower case words
print(" ".join(word))
    







        