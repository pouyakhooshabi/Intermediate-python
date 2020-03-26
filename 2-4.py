age = int(input())
a=0
b=0
while age != -1:
    
    
    if age > a:
        b= a
        a= age
    
    age = int(input())

print (a , b)        
