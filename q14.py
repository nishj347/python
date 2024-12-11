#14.Write a Python program to find the second largest number in a list.
def secondlargest(l):
    l=list(set(l))
    l.sort(reverse=True)
    return l[1] if len(l)>1 else None
    
number=[332]
print("the second largest number is :",secondlargest(number))
