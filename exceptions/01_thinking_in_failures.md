## Operation: int(input())

Possible failures:
- User enters letters or symbols 
- Too large number
- Empty input


Why this matters:
- It matters the user can enter a number incorrectly or something not supported

## Operation: a/b

Possible failures:
- Divisor is zero
- One or both values are not numeric
- Values originate from invalid user input

Why this matters:
- Division by zero is impossible
- We can divide only number

## Operation: Reading a file

Possible failures(so many):
- File not found
- Invalid path
- Permission denied
- File is empty
- Encoding errors

Why this matters:
- A file is an external ressources, we don't have control over, without proper error handling it would make the program crash

## Operation: Accessing a dictionary key

Possible failures:
- Key does not exist
- Key is None
- Wrong data structure type

Why this matters:
- Dictionaries often come from external data (JSON, APIs)
- Missing keys can cause runtime errors

## Operation: Calling an external API (simulated)

Possible failures:
- Network timeout
- Request denied
- Invalid response format
- Missing expected data
Why this matters:
- API are outside our system, and can bring a lot of unexpected variables (APIs can fail even when your code is correct)
