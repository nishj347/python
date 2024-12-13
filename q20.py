# 26.Write a Python program to count the number of vowels in a string.
def countv(char):
    count=0
    vowel="aeiouAEIOU"
    for i in char:
        if i in vowel:
            count+=1
    return count        
    
  
char="i am a preety girl"
print(countv(char))
