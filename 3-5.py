theletter = input()
countsmall =0
countbig = 0  
for i in theletter:
    if i.islower():
        countsmall = countsmall + 1
    elif i.isupper():
        countbig = countbig + 1
if countbig > countsmall:
    print (theletter.upper())
else:
    print (theletter.lower())           

        



   