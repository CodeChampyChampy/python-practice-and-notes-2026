log = "User entered password incorrectly"

#So I should use replace method

def print_hidden_incorrect_password_in(myVariable):
    return print(myVariable.replace("password", "******"))

print_hidden_incorrect_password_in(log)