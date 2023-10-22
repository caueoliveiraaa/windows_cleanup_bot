# Python has the following data types built-in by default, in these categories:

# ++++++++++++++++ categories ++++++++++++++++
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType
# +++++++++++++++++++++++++++++++++++++++++++++


# Print the data type of the variable x:
print('++++++++ All data types ++++++++')

#  Integer
x = 5
print(x)
print(type(x))

# String
x = "Hello World"
print(x)
print(type(x)) 

# Float
x = 20.5
print(x)
print(type(x)) 

# Complex
x = 1j
print(x)
print(type(x)) 


# list
x = ["apple", "banana", "cherry"]
print(x)
print(type(x)) 


# tuple
x = ("apple", "banana", "cherry")
print(x)
print(type(x)) 


# range
x = range(6)
print(x)
print(type(x)) 


# dictionary 
x = {"name" : "John", "age" : 36}
print(x)
print(type(x)) 


# set
x = {"apple", "banana", "cherry"}
print(x)
print(type(x)) 


# frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) 


# Boolean
x = True
print(x)
print(type(x)) 


# bytes
x = b"Hello"
print(x)
print(type(x)) 


# bytearray
x = bytearray(5)
print(x)
print(type(x)) 


# memoryview
x = memoryview(bytes(5))
print(x)
print(type(x)) 


# NoneType
x = None
print(x)
print(type(x)) 
