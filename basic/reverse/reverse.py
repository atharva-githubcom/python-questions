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

#2.Logic to Check Palindrome

s = input("Enter the string or number: ")  # take input from user
# compare the original string with its reverse
if s == s[::-1]:  
    print("Palindrome")  # print if input is a palindrome
else:
    print("Not Palindrome")  # print if input is not a palindrome

#s == s[::-1]: explanation
#start → where to begin counting (inclusive) 
#end → where to stop counting (exclusive)
#step → how many indices to skip each time
#step < 0 → go backwards, useful for reversing strings

#3.Find the largest number in list

S = list(map(int, input("Enter numbers separated by space: ").split()))
# Take input from user as string, split by space into a list of strings,
# then convert each element to integer using map(), and finally convert map to list.
largest = S[0]  
# Assume the first number in the list is the largest for now
for num in S:  
    # Loop through each number in the list
    if num > largest:  
        # If the current number is bigger than largest
        largest = num  
        # Update largest with this number
print("The largest number is:", largest)  
# After the loop, print the largest number found
#List: 10, 25, 5, 40, 15
#Start: largest = 10
#Step 1: Compare 25 > 10 → Yes → largest = 25
#Step 2: Compare 5 > 25 → No → largest = 25
#Step 3: Compare 40 > 25 → Yes → largest = 40
#Step 4: Compare 15 > 40 → No → largest = 40
#Result: largest = 40

#4.Addition of the total number in list

s = list(map(int, input("Enter the numbers: ").split()))
total = 0  
# Initialize a variable to store the sum of numbers
for i in s:  
    # Loop through each number in the list
    total = total + i  
    # Add current number to total
print("The total of numbers is:", total)  
# After the loop, print the sum of all numbers


#5.finding the vowel in list 

# Take input string from user and convert it to lowercase
v = input("Enter the string: ").lower()  # converts all letters to lowercase for case-insensitive checking

# Initialize a counter to keep track of vowels
count = 0

# Loop through each character in the string
for i in v:
    # Check if the current character is a vowel
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count = count + 1  # increment the counter if vowel found

# Print the total number of vowels
print("Number of vowels:", count)
