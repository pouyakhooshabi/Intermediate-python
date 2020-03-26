selecnum= int(input())
c=0
for i in range(1, selecnum):
    if selecnum % i == 0:
        c = c+1

if c == 1:
    print ("prime")
else:
    print("not prime")    
        

