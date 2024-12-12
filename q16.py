# 16.Write a Python program to remove duplicates from a list.
def remove(l):
   l=list(set(l))
   print(l)
    
    
number=[342,32,12,342,12,21,21,21,21,342,32]
remove(number)
