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