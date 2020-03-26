import random
guess = random.randint(1,99 )
print(guess)
answer = input()
a=1
b=99
while answer != "d":
    if answer == "b":
        a = guess 
    elif answer == "k":
        b = guess 
    guess = random.randint(a, b )
    print(guess)
    answer = input()        
    
print ("Done!!")   