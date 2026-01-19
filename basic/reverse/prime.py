#prime number 
n = int(input("Enter the number: "))

if n <= 1: # number less then 1 or 1 is not prime
    print("Not prime")
else:
    for i in range(2, n): #number from 2  check this 
        if n % i == 0: #this check that n % i which is number in loop 
            print("Not prime")
            break
    else: # nested if conditional statement.
        print("Prime")