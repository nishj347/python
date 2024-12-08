# Write a Python program to convert a temperature from Fahrenheit to Celsius.
def demo(num):
    celsius=(num-32)/1.8
    return celsius

num=int(input("enter the number: "))
print("celsius to faherenite",demo(num))
