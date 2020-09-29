#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
a=input("Enter a number")
a=float(a)
b=math.floor(a)
if a==b:
    print("A is an integer")
else:
    print("A is not an integer")
