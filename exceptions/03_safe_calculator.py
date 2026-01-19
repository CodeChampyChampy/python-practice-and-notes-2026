
def basic_calculator():
    try:
        num1 = int(input("Enter the number 1: "))
        num2 = int(input("Enter the number 2: "))
    except ValueError:
        print("Invalid number entered")  
        return
    
    operation = input("Choose an operation: '+' ,'-', '*', '/' : ")

    try: 
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            print("Invalid operator !")
            return
    except ZeroDivisionError as zde:
        print("Error !", zde)
        return
    else:
        print(result)


basic_calculator()