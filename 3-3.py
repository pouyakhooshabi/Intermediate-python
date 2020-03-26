my_list = []
i = 0
while i<10:
    my_list.append(input())
    i += 1
fin_list= []   
for x in my_list:
    x= x.lower()
    x= x.capitalize()
    fin_list.append(x)
for names in fin_list:    
    print (names)