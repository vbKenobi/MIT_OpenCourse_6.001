#Problem Set 0:
#Write a program that does the following in order:
#1. Asks the user to enter a number “x”
#2. Asks the user to enter a number “y”
#3. Prints out number “x”, raised to the power “y”.
#4. Prints out the log (base 2) of “x”.

import numpy as np

#Taking in user input:
x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))

print("x**y = ", x**y)
print("Log base 2 of x = ", np.log2(x))
