#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
import math
a=input("Enter side 1 length")
b=input("Enter side length 2")
c=input("Enter side length 3")
a=float(a)
b=float(b)
c=float(c)
x=math.pow(a,2)
y=math.pow(b,2)
z=math.pow(c,2)
if z>y and x:
    h=float(z)
    j=float(y)
    k=float(x)
elif y>z and x:
    h=float(y)
    j=float(z)
    k=float(x)
elif x>z and x:
    h=float(x)
    j=float(z)
    k=float(x)


if h==(j+k):
    print("that is a right triangle")
elif h>(j+k):
    print("that is an acute triangle")
elif h<(j+k):
    print("that is an obtuse triangle")
