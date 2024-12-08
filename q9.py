# Write a Python program to print the Fibonacci sequence up to a given number of terms.
def fibonaci(num):
    if num<=0:
        return "invalid"
    elif num==1:
        return [0]
    elif num==2:
        return [0,1]
        
    fib=[0,1]
    for i in range(2,num):
        nextterm=fib[-1]+fib[-2]
        fib.append(nextterm)
    return fib
    
num=int (input("enter the number:"))
print("series:",fibonaci(num))
