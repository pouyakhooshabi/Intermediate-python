s1=''
x=input()
for letter in (x):
    if letter == 'h':
        x = x[x.index('h')+1:]  
        s1 += 'h'    
        break
for letter in (x):
    if letter == 'e':
        x = x[x.index('e')+1:]  
        s1 += 'e'   
        break 
for letter in (x):
    if letter == 'l':
        x = x[x.index('l')+1:]  
        s1 += 'l'    
        break
for letter in (x):
    if letter == 'l':
        x = x[x.index('l')+1:]  
        s1 += 'l'  
        break
for letter in (x):
    if letter == 'o':
        x = x[x.index('o')+1:]  
        s1 += 'o'   
        break 
if s1 == 'hello':
    print('YES')
else :
    print('NO')    
