# Take input from the user for number of rows
n = int(input("Enter number of rows: "))

# Outer loop: controls the number of rows
# i will go from 1 to n (inclusive)
for i in range(1, n + 1):

    # Inner loop: controls number of stars in each row
    # It runs 'i' times, so stars increase row by row
    for j in range(i):

        # Print star in the same line
        # end=" " prevents moving to a new line after printing *
        print("*", end=" ")

    # This print() moves the cursor to the next line
    # After finishing one row of stars
    print()