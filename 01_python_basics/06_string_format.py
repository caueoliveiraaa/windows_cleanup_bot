# We can combine strings and numbers by using the format() method.
# The format() method takes the passed arguments, formats them,
# and places them  in the string where the placeholders {} are.

age = 36
text = "My name is Smith, and I am {}"
print(text.format(age))

# The format() method takes unlimited number of arguments,
# and are placed into the respective placeholders:
phonenumber = 55584218
zipcode = 51
social_seurity = 18715158156
txt = 'Phone number: {}, zip code: {}, social security number: {}.'
print(txt.format(phonenumber, zipcode, social_seurity))
# You can indicate where the variables go with indexes
txt = 'Phone number: {0}, zip code: {1}, social security number: {2}.'
print(txt.format(phonenumber, zipcode, social_seurity))
# And you can change the positions as you will
txt = 'Phone number: {2}, zip code: {1}, social security number: {0}.'
print(txt.format(phonenumber, zipcode, social_seurity))
