# Write a Python program to check whether a string is a palindrome.
string=input("enter a string: ")
if string == string[::-1]:
    print("the string is palindrome")
else:
    print("the string is not palindrome")
