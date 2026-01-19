## Operation: int(input())

Possible failures:
- Not a number entered (letter or special character)
- Too large number
- User enter 'none'

Why this matters:
- It matters the user can enter a number incorrectly or something not supported

## Operation: a/b

Possible failures:
- division by 0
- a/b is not a number 
- user input

Why this matters:
- Division by zero is impossible
- We can divide only number

## Operation: Reading a file

Possible failures(so many):
- File not found
- Invalid path
- Don't have the permission
- ???

Why this matters:
- The file is an external ressources, we don't have control over, without proper error handling, it would make the program crash

## Operation: Accessing a dictionary key

Possible failures:
- Key doesn't exist
- Key is 'none'
- ???

Why this matters:
- To manage properly key/value system, that can rapidly be complex and pose threat 

## Operation: Calling an external API (simulated)

Possible failures:
- timeout
- request denied
- ...

Why this matters:
- API are outside our system, and can bring a lot of unexpected variables
