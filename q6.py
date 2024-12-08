# Write a Python program to calculate the sum of all digits in a given number.
def add(num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit
        num//=10
    return sum    

        
num=int(input("enter the number:"))
print(f"sum of digits", add(num))
    
    
