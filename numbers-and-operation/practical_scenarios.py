#Exercise 13 — Total price

def calculate_total_price(unit_price, quantity):
    return unit_price * quantity

#Exercise 14— Average value
def average_two_num(num1, num2):
    return (num1+num2)/2

#Exercise 15 — Duration conversion
'''
1)We enter an integer for the seconds 
2)We floor divide by 60 and take the result as minutes
3)We keep the remaining seconds with modulo
4)We return the conversion
'''
def convert_seconds_to_minutes(sec):
    return (sec//60, sec%60)

#Exercise 16 — Rounded result
def round_number_to(num_to_round, number_of_decimal):
    return round(num_to_round, number_of_decimal)
