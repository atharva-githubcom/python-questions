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