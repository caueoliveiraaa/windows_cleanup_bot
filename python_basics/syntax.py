"""
NOTE: Python was created in 1991 by Guido van Rossum.
    
    It's used for:
        - web development (server side)  
        - software development
        - mathematics
        - system scripting
    
"""

# Comments can be placed at the end of a line,
# and Python will ignore the rest of the line

# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.

# This is a comment.
integer_numer = 5 
# String variables can be declared either by using single or double quotes:
text = 'Hello, world'

print('Printing the text variable:')
print(text) # This is a comment.


# If you want to specify the data type of the variable,
# this can be done with casting.

x = str(3) # '3'
y = int(3) # 3
z = float(3) # 3.0

# You can get the data type of a variable with the type() function.
print('Printing the types:')
print(type(x))
print(type(y))
print(type(z))


# Variable names are case-sensitive.
# This will create two variables:
a = 4
A = 40 # A will not overwrite a


# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"