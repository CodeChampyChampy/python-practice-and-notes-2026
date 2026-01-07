email = "  USER@GMAIL.COM "

# Fun fact, I thought it didn't matter how you write your email because it worked whatever the case. 
'''
I have to clean and check if it's a gmail adress
1) Clean (no space with strip, lowercase)
2) Check if it's a gmail address. We recognize a gmail adress because it has "@gmail.com" at the end
'''

def is_a_valid_gmail_adress(mail):
    #Clean
    mail = mail.strip().lower()
    #Check
    return print(mail.endswith("@gmail.com"))

is_a_valid_gmail_adress(email)