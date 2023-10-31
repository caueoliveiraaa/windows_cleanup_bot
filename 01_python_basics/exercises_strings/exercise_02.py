# Exercise 2:
# Write a program that takes a string as input and prints its
# characters in reverse order.


string = input('String: ')
string = list(string)

for index in range((len(string) - 1), -1, -1):
    print(string[index])
