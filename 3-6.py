Thename = input()
Thename = Thename.lower()
reverseit= Thename[::-1]
if Thename == reverseit:
    print('palindrome')
else:
    print('not palindrome')    
