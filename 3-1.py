ourstr = input()
s= ourstr.lower()
#d= s.replace('a','')
lst = ['a','e','i','o','u']
for i in lst:
    s= s.replace(i,'')
d= ''
for letter in s:
    d += '.'+ letter

print (d)    

