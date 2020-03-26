a = int(input())
b = a//10
firstnum= b//10
secondnum= b%10
thirdnum= a%10
print(2*(thirdnum*100 + secondnum*10+ firstnum))