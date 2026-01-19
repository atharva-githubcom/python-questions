#1.Write a Python program to reverse a given string without using built-in reverse functions.

s = input("enter the string to reverse: ")   # takes a string input from the user
rev = ""                                     # creates an empty string to store reversed string
for i in s:                                  # loop runs for each character in the input string
    # i takes one character at a time from s
    # first iteration: i = first character of string
    # next iterations: i = next characters one by one
    
    rev = i + rev                            # adds current character 'i' in front of 'rev'
    # example:
    # if i = 'y' and rev = 'p'
    # rev = 'y' + 'p' → 'yp'
    # this prepending reverses the string step by step

print(rev)                                  # prints the final reversed string

# This loop iterates through each character of the string and prepends it to a new string,
# which results in the reversed string.
