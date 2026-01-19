

def is_user_input_valid(): #read_integer_from_user() would be fine
    user_input = input("Enter a number: ")
    try: 
        user_input = int(user_input)
        print(f"{user_input} is valid")
    except ValueError:
        print(f"Error, '{user_input}' is not a valid number")

is_user_input_valid()
