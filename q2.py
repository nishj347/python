# Write a Python program to find the factorial of a number using a loop.
n=int(input("eneter the number:"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(f" factorial is {factorial}")
