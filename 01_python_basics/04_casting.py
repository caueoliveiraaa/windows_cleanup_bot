# NOTE:
# There might be times when you want to specify a type onto a variable.
# This can be done with casting. Python is an object-oriented language,
# and as such it uses classes to define data types, including its
# primitive types.

# Casting in Python is therefore done by using constructor functions:
# int() - contructs an integer number from an integer literal, a float
# literal (by removing all decimals), or a string literal (providing 
# the string represents a whole number) 
# float() - constructs a float number from an integer literal, a float
# literal or a string literal (providing the string represents a float
# or an integer)
# str() - constructs a string from a wide variety if data types, including
# strings integer literals, and float literals

x = int(1)     # will be 1
y = int(2.8)   # will be 2
z = int("3")   # will be 3
print('Converting to integers:')
print(x)
print(y)
print(z)

print('Converting to floats:')
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)
print(w)

print('Converting to strings:')
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'