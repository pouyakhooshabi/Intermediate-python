letter= input() 
if 'AB' in letter and letter != 'BABA':
    a= letter.find('AB')
    b= letter[0:a]+letter[a+2:]
    if 'BA' in b:
        print('YES')
    else:
        print('NO')
else: 
    print ('NO')    

    
