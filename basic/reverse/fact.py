# Take a number as input from the user
n = int(input("Enter the number: "))

# Initialize factorial value to 1
# (because factorial is multiplication and 1 is the neutral value)
fact = 1

# Loop from 1 to n (inclusive)
for i in range(1, n + 1):
    # Multiply current factorial value with i
    fact *= i

# Print the final factorial result
print("Factorial is:", fact)
