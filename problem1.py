#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"
n = input("Please enter one number")
num = input("Please enter a second number")
n = int(n)
num = int(num)
if n % num == 1:
    print("The number is odd")
if n % num == 0:
    print("The number is even")

