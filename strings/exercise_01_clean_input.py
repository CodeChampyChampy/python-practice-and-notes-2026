text = "   HeLLo WoRLd   "

# I think I have to use strip and lower methods

def print_clean_and_lowercase(myString):
    myString = myString.strip().lower()
    return print(myString)

print_clean_and_lowercase(text) #to replace the original string I have to assign the new value
