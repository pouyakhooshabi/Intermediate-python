a = input()
my_list = []
for i in range(0,len(a)):
    if i%2 == 0:
        my_list.append(int(a[i]))
my_list.sort() 

x = ''
x += str(my_list[0])
for i in range(1, len(my_list)):
    x += '+'
    x += str(my_list[i])
print(x)