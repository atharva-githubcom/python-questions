#Write a Python program to count how many even and odd numbers are present in a given list.
# Take numbers from user separated by space and convert them to a list of integers
num = list(map(int, input("Enter the numbers: ").split()))

# Initialize counters for even and odd numbers
count_even = 0
count_odd = 0

# Loop through each number in the list
for i in num:
    # Check if the number is even
    if i % 2 == 0:
        count_even += 1   # increase even count
    else:
        count_odd += 1    # increase odd count

# Print the results
print("Even count:", count_even)
print("Odd count:", count_odd)
    