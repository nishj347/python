def prime(start,end):
    for i in range (start,end+1):
        if num>1:
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    break
                else:
                    print("prime")
            
start=int(input("enter the number:"))
end=int(input("enter the number:"))
prime(start ,end)
