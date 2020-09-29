#! python3 

# Have the user enter a number. 
# Use an if...elif statement to determine if the number is 
# a) larger than 1000 
# b) larger than 100 
# c) larger than 10 
# d) larger than 0 
# Output must match one of the valid output statements listed
# (2 points)

# Inputs:
# a number

# Output is a single number that represents a range of numbers:
# "3" : The number is equal to 1000 or is larger than 1000
# "2" : The number is 100 or a number up to 1000 
# "1" : The number is 10 or a number up to 100 
# "0" : The number is 0 or a number up to 100 
a=input("Enter a number")
a=float(a)
if a>=1000:
    print("larger than 1000")
elif 1000>a>=100:
    print("larger than 100") 
elif 100>a>=10:
    print("larger than 10")
elif 10>a>=0:
    print("larger than 0")
elif a<0:
    print("a is less than 0")


if a>=1000:
    print("3")
elif 1000>=a>=100:
    print("2") 
elif 100>=a>=10:
    print("1")
elif 100>=a>=0:
    print("0")
