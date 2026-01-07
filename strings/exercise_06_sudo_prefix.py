command = "sudo apt update"

def does_start_with_sudo(myString):
    return print(myString.startswith("sudo"))

does_start_with_sudo(command)