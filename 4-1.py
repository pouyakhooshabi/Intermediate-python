a= int(input())
i = 0
list_num= []
while i < a:
    list_num.append(int(input()))
    i += 1     
import math
fin_list= []
for i in list_num:
    fin_list.append(math.sqrt(i))
import decimal
lst= []
for i in fin_list:
    c = decimal.Decimal(i)
    lst.append(round(c,6))   
string_lst= []
for i in lst:
    string_lst.append(str(i))
new_st_list= []    
for i in string_lst:
    c= i.find('.')
    d= i[c:c+5]
    e= i[0:c]
    print (e+d)   

      
