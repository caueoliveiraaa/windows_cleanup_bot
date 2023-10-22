# NOTE: There are three numeric types in Python: int, float and complex

# Variables of numeric types are created when you assign a value to them
var_1 = 23  # int
var_2 = 2.8 # floar
var_3 = 1j  # complex

# int, or integer, is a whole number, positive or negativa, without decimals, 
# of ulimited length.
x = 1
y = 3215181321518848
z = -33251515
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# float, or floating-point number is a number, positive or negative, counting 
# on or more decimals
x = 1.10
y = 1.0
z = -35.59
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# float can also be scientific numbers with an "e" to indicate the power of 10
x = 35e5
y = 12e4
z = 81.7e100  
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# complex numbers are written with a j as the imaginary part
x = 3+5j
y = 5j
z = -5j  
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# Python does not have a random() function to make a random number, but
# Pythonhas a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1, 10))