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
