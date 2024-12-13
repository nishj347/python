# 18.Write a Python program to find the common elements between two lists.

def common(list1,list2):
    return list(set(list1) & set(list2))
    
  
list1=[342,32,12,342,12,21,21,21,21,342,32]
list2=[23,13,2,1,3,112,12,21,21]
print(common(list1,list2))
