# Creating an empty list for email inbox
inbox = []

# Creating class email with attributes email address, subject line and email content
class Email():
    has_been_read = False # this is for unread emails

    def __init__(self, email_address, subject_line, email_content): 

        """initiliasing the attributes for email"""

        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    
    def show_message(self): # this function shows the full email content

        """Prints out the full content of the email"""

        return f'\nFrom: {self.email_address}\nSubject: {self.subject_line}\n{self.email_content}\n'

    def mark_as_read(self):

        """Marks the email as read when has_been_read  function is true"""

        self.has_been_read = True


    def populate_inbox(self):

        """Populating the inbox with email"""

        inbox.append(self)


# Greeting the user and instructing them to be the sender of the email
print("\nHello user, welcome to the email simulation!\nLet's pretend you are sending an email to one person.\n")


# This loop asks the user to send multiple emails
while True:
    message = input("Would you like to send an email (Y/N): ")

    if message == "Y":
        email = input("\nEnter your email: ")

        if "@gmail.com" in email: # must have @gmail in the string
            subject = input("Subject: ")
            content = input("Write your message: ")  
            email_list = Email(email, subject, content)
            email_list.populate_inbox()
        else:
            print("Please enter a valid email.")
    if message == "N":
        break
    
    else:
        print("")


# Instructing the user to be the receiver of the email
print("\nLets now pretend you are the person receiving the email.")


# This function displays the unread email
def unread_emails(unread):
    print("\nEmail:")

    for count, item in enumerate(unread):
        if unread[count].has_been_read == False:
            print(f'{str(count)}    {item.subject_line}')


# This function displays the read email
def read_emails(read):
    print("\nEmail:")

    for count, item in enumerate(read):
        if read[count].has_been_read == True:
            print(f'{str(count)}    {item.subject_line}')



# This function gives the user multiple decisions to read emails. 

def read_email(inbox_number):
    while True:

        # Giving the user the option to choose between reading unread emails, read emails and exit.
        page = input("\nPlease select the following option:\nView inbox: 0\nView read inbox: 1\nExit: 2\nEnter here: ")
        print("")

        if page == "0": # opens up unread emails
            unread_emails(inbox_number)
            index = int(input(f'\nType the index of the email to view (0 to {len(inbox_number) - 1}): '))

            if index >= 0 and index < len(inbox_number) and inbox_number[index].has_been_read == False: # giving the user the option to choose to read their email based on the index
                email_index = (inbox_number[index])
                print(email_index.show_message())
                email_index.mark_as_read()

            elif index >= 0 and index < len(inbox_number) and inbox_number[index].has_been_read == True:
                print("\nAll email has been read. See option 1 to view read inbox")

            else:
                print("\nThis email does not exist.\n") # index number outside the range will loop the user back

        elif page == "1": # opens up read emails
            read_emails(inbox)
            index = int(input(f'\nType the index of the email to view (0 to {len(inbox_number) - 1}): '))

            if index >= 0 and index < len(inbox) and inbox_number[index].has_been_read == True: # giving the user the option to choose to read their email based on the index
                email_index = (inbox[index])
                print(email_index.show_message())
            elif index >= 0 and index < len(inbox) and inbox_number[index].has_been_read == False: # giving the user the option to choose to read their email based on the index
                print("\nEmail does not exist in this inbox. See option 0 to view unread inbox.")

            else:
                print("\nThere is no email\n") # index number outside the range will loop the user back
        
        elif page == "2": # leaves the program
            print("You have logged out. Have a nice day")
            break

        else:
            print("Try again")


read_email(inbox)


