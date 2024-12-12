#15.Write a Python program to reverse a list without using reverse() method.

def reverse(l):
    return l[::-1]
    
    
number=[332,32,12,342,12,21]
print("reversed list",reverse(number))
