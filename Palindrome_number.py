num = int(input("Enter a number: "))

original = num      # Save the original number that user input

reverse = 0

while num>0:                # Reverse the number
    digit = num % 10        # get the last number
    reverse = reverse * 10 + digit      
    num = num // 10         # Remove last number
print(reverse)
       

if original==reverse:       # Check if the reverse 
    print("Palindrome.")    # number and original number 
                            # is same, then palindrome.
else:
    print("Not Palindrome")