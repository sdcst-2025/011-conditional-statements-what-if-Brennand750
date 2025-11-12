#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""
a = input("Please input a number")
a = int(a)
if a < 100:
    print(a,"is smaller than 100")
if a > 100:
    print(a, "is grater than 100")
if a == 100:
    print(a, "is equal to 100")
    