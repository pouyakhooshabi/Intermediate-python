def devidenum(a):
    inpt = a
    n= 1 
    c= 0 
    while n <= inpt:
        if inpt % n == 0:
            c = c+1
        n = n+1
    return (c)
score1= int(input())
score2= int(input())
score3= int(input())
score4= int(input())
score5= int(input())
score6= int(input())
score7= int(input())
score8= int(input())
score9= int(input())
score10= int(input())
score11= int(input())
score12= int(input())
score13= int(input())
score14= int(input())
score15= int(input())
score16= int(input())
score17= int(input())
score18= int(input())
score19= int(input())
score20= int(input())
lst = [score1,score2,score3,score4,score5,score6,score7,score8,score9,score10,score11,score12,score13,score14,score15,score16,score17,score18,score19,score20]
Biggest = 0
thescore = 0
for i in lst:
    maqsoom = devidenum(i)
    if maqsoom > Biggest or (maqsoom == Biggest and i > thescore) : 
        Biggest =  maqsoom
        thescore = i
print(thescore, Biggest)            
