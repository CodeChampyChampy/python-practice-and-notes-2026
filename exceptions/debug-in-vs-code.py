'''Here is a **short Python code with a deliberate bug**, **short** and **suitable for beginners** 🐍. 
Your goal: **find and correct the error**.  
tip: use the red circle before entering debug mode to select a line 
'''

def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

list = [10, 15, 20]
print("The average is:", average(list))
average([20, 5])
'''
Note (important)
The problem here is the case where we enter an empty string, we sould get a ZeroDivision Erro. 
It show that:

- A bug may not appear immediately

- You have to think about edge cases
(eg: if not list: is a Python way of testing an empty list)
'''

