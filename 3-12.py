number_voc= int(input())
i = 0
group_voc = []
while i < number_voc:
    group_voc.append(input())
    i += 1 
i = 0  
new_gplist= []    
for i in group_voc:
    new_gplist.append(i.split()) 
dirc={} 
i = 0
while i < number_voc:
    dirc[new_gplist[i][0]]= new_gplist[i][1]
    i += 1 
sentence= input()       
sent_list= sentence.split()
fin_list= []
for i in sent_list:
    if i in dirc:
        fin_list.append(dirc[i])
    else:
        fin_list.append(i)  
for x in fin_list:
    print (x, end=' ')
