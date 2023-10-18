# Q5. Write a recursive function to check if a given string is a palindrome.

def is_palindrome(string):
    
    if len(string) <= 1:
       
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
        
    else:
        return False

string = input("Enter a string: ")

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
