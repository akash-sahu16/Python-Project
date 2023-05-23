print("Enter you email id to Validate")
email = input("Email id: ")
k, j, d = 0, 0, 0

if len(email) >= 6: # This checks wether the length of the email is greater than or equal to 6 characters.
    if email[0].isalpha(): # This line checks wether the first character of the mail is alpahbet.
        if "@" in email and email.count("@") == 1: #This line verifies that the "@" sign appears precisely once and is present in the email. It makes sure there is only one "@" sign in the email.
            if email[-4] == "." or email[-3] == ".": #This line checks if the fourth character from the end or the third character from the end of the email is a period (".") character.
                for i in email: #This line initiates a loop that iterates over each character (i) in the email.
                    if i.isspace(): #This line checks if the current character is a whitespace character. It sets the value of 'k' to 1 if a whitespace character is found.
                        k = 1
                    elif i.isalpha(): #This line is an "else if" condition that checks if the current character is an alphabet letter.
                        if i == i.upper(): #This line checks if the current character is an uppercase letter. It sets the value of 'j' to 1 if an uppercase letter is found.
                            j = 1
                    elif i.isdigit():#This line is an "else if" condition that checks if the current character is a digit.
                        continue
                    elif i == "_" or i == "." or i == "@":# This line is an "else if" condition that checks if the current character is either an underscore ("_"), a period (".") or an "@" symbol. These characters are allowed in the email address.
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:#checks if any of the variables k, j, or d is equal to 1.
                    print("Invalid Email-ID")
                    print("please enter valid email id (eg : xyz@gmail.com) ")
                else:
                     print("right email")    
            else:
                print("Invalid email")
                print("please enter valid email id (eg : xyz@gmail.com) ")
        else:
            print("Invalid Email-ID")
            print("Note :'@' symbol is missing or it should appear only one time")
    else:
        print("Invalid Email-ID")
        print("Note : The first character of the mail shouldn't be greater ")
else:
    print("Invalid Email-ID")
    print("Note : The length of the id should be greater than 6")
