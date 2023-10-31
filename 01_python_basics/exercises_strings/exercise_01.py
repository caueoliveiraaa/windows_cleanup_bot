# Given a string, print it in reverse using negative indexes.

string = '123456789'
string = list(string)
for index in range((len(string) - 1), -1, -1):
    print(string[index])
