number= int(input())
Num_of_comp= input()
Num_of_comp= Num_of_comp.split()
int_list= []
for i in Num_of_comp:     
    int_list.append(int(i))
count= 0
for i in int_list:
    if i < 3:
        count += 1
print (count//3)        

  