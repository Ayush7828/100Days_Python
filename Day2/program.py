'''
Data Types
Numbers
Operators
Type Conversion
f-String

'''

# Data types

# int myNum = 5;               // Integer (whole number)
# float myFloatNum = 5.99f;    // Floating point number
# char myLetter = 'D';         // Character
# boolean myBool = true;       // Boolean
# String myText = "Hello";

# type error
# num_char = len(input("What is your name ? "))
# print("Hello "+num_char+"thankuu")

# TypeError: can only concatenate str (not "int") to str
# check type of datatype use type()-- function

# like

num_char = len(input("What is your name ? "))
new_num_char = str(num_char)
# print("Hello "+num_char+"thankuu")
# type(num_char)
print(type(num_char))
print("Hello "+new_num_char+" ", "Thnakuu")

# output:  <class 'int'>


# output- What is your name ? ayush
# <class 'int'>
# Hello 5  Thnakuu
