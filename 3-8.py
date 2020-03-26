import math
my_list= []
i=0 
while i < 3:
    my_list.append(int(input()))
    i += 1
sum1= sum(my_list) 
count1= len(my_list)
avg= sum1/count1
a=0
b=0
for x in my_list:
    a= abs(x-avg)
    b= b+a
print(math.floor(b))


