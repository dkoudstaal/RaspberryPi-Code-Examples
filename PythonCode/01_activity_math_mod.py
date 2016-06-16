## Activity Math Module
## /home/pi/python_programs/01_activity_math_mod.py
## Peter Scarlett 25 Feb 2016

'''
In this activity you will manipulate the mathematics module.
You will learn to manipulate and program with mathematical formulas
in Python.
Follow the instructions in the comments.

At the end of this file are detailed instructions how to submit your work!
'''

import os
import math

## Instructions

'''
If you type help(math) in the shell you will see all the available
functions in the math module.
a more detailed description of the math module is on the official
Python site:
https://docs.python.org/3.4/library/math.html#module-math

Below is a demonstration of the factorial function.
factorial 4 is also written in text books as 4!
This is what 4! means:
    factorial 4 = 1x2x3x4
    and of course 1x2x3x4 = 24

Give my_number different values and see what the answer is.
'''

my_number = 6
## Calculation of factorial of my_number:
factorial_answer = math.factorial(my_number)
print("The factorial of", my_number, "is:", factorial_answer)

## Write below the code similar to the two lines above to
## Print the square root of the variable my_number.
## Name the variable containing the square root value square_root

## Calculation of square root of my_number:
## Write your code below this comment.

square_root = math.sqrt(my_number)
print("the square root of", my_number, "is:", square_root)

## After you have created the code for the square root write the code of
## any three mathematical functions of your choice from the math module
## Write your code below this comment.
squared = math.pow(my_number, 2)
print(my_number, "squared is", squared)

sine = math.sin(my_number)
print("the sine of", my_number, "is", sine)

h_tangent = math.tanh(my_number)
print("the hyperbolic tangent of", my_number, "is", h_tangent)

'''
How to submit your code:
    1 - Change my name at the top of this file to your name.
    2 - Do not delete any of the instructions of this file.
    3 - Change the value of my_number to 6
    4 - save the file but do not change the name of the file
    5 - Upload the file to the Moodle Task 2 
'''
