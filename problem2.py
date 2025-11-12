#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
"""
enter a number: float
how do you separate the decimal part
if the decimal part is 0 then 
    it is not an integer 
else 
    it is an integer

"""
x = input ("Enter a number")
x = float(x)
integer_part = int(x)
decimal_part = x - integer_part
if decimal_part == .0:
    print("It is an integer")
else:
    print("It is not an integer")