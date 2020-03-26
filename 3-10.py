num_pc= int(input())
i = 0
mainlist= []
while i < num_pc:
    mainlist.append(input())
    i += 1
New_list= []    
for i in mainlist:
    New_list.append(i.split())
c = 0
while c < num_pc:
    New_list[c][0]=int(New_list[c][0])
    New_list[c][1]=int(New_list[c][1])
    c += 1        
i = 0
j = i+1
flag = 0
while i< num_pc and flag ==0:
    while j< num_pc and flag ==0:     
        if New_list[i][0] > New_list[j][0] and New_list [i][1] > New_list [j][1]:
            j += 1
        elif New_list[i][0] < New_list[j][0] and New_list [i][1] < New_list [j][1]:
            j += 1
        else:   
            print('happy irsa') 
            flag = 1
    i += 1
    j = i+1
if flag == 0:    
    print ("poor irsa")
        