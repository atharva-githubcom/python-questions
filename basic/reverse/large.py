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
