#Exercise 5
def calculate_two_numbers_basic_operation(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return (addition, subtraction, multiplication, division)

#Exercise 6
def calculate_floor_division_two_numbers(num1, num2):
    return num1 // num2

#Exercise 7
def modulo(num1, num2):
    return num1 % num2

#Exercise 8
def power(base, exponent):
    return base ** exponent

print(calculate_two_numbers_basic_operation(4, 2))
print(calculate_floor_division_two_numbers(12, 5))
print(modulo(7, 3))
print(power(2, 3))