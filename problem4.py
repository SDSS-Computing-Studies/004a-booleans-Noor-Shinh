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
a=int(a)
b=int(b)
c=int(c)
x=math.pow(a,2)
y=math.pow(b,2)
z=math.pow(c,2)
if z>y and x:
    h=int(z)
    j=int(y)
    k=int(x)
elif y>z and x:
    h=int(y)
    j=int(z)
    k=int(x)
elif x>z and x:
    h=int(x)
    j=int(z)
    k=int(x)


if h==(j+k):
    print("that is a right triangle")
elif h<(j+k):
    print("that is an acute triangle")
elif h>(j+k):
    print("that is an obtuse triangle")
