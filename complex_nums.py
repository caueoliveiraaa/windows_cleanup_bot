"""
Complex numbers are the numbers that are expressed in the form
of a + ib where, a,b are real numbers and  'i' is an imaginary number
called “iota”.
The main application of these numbers is to represent periodic motions
such as water waves, alternating current, light waves, etc., which rely
on sine or cosine waves, etc.
"""


# The quickest way to define a complex number in Python is by typing its
# literal directly in the source code

var = 3 + 2j
print(f'Value of var {var} | type of var {type(var)}')

# It's possible to create complex numbers with floating numbers
var2 = 3.14 + 2.71j
print(f'Value of var2 {var2} | type of var2 {type(var2)}')

# It's possible to upper case J
var3 = 3.14 + 2.71J
print(f'Value of var3 {var3} declared with J | type of var3 {type(var3)}')
