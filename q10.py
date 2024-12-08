# 10.Write a Python program to print a multiplication table of any number.
def table(num):
    for i in range (1,11):
        print(num*i)
        
num=int(input("enter the number:"))
table(num)
