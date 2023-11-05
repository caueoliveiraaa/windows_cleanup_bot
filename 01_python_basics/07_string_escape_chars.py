# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside
# a string that is surrounded by double quotes:
txt = "We are the so-called \"Vikings\" from the north."
print(txt) # We are the so-called "Vikings" from the north.

# Single Quote \
txt = 'It\'s alright.'
print(txt) # It's alright.

# Backslash \\
txt = "This will insert one \\ (backslash)."
print(txt) # This will insert one \ (backslash).

# New Line \n
txt = "Hello\nWorld!"
print(txt) # Hello
           # World!

# Carriage Return \r, It moves the cursor to the beginning
# of the current line without moving to the next line.
txt = "Hello\rWorld!"  
print(txt) # World!

# tab \t
txt = "Hello\tWorld!"
print(txt) # Hello   World!

# Backspace \b
txt = "Hello \bWorld!"
print(txt) # HelloWorld!

# Octal value \ooo
# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

# Hex value \xhh
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 