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


# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)


# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# If you create a variable with the same name inside a function,
# this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)


# Normally, when you create a variable inside a function, that variable is local,
# and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "incredible"

print("Python is " + x)


# To change the value of a global variable inside a function,
# refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "amazing"

myfunc()
print("Python is " + x)
