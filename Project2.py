import hashlib
import csv
def hash_password_hack(input_file_name , output_file_name):
    #section 1: input file and break it to name and password
    with open(input_file_name , 'r' ) as f:
        reader = csv.reader(f)
        file = open(output_file_name ,'w')
        name= []
        password=[]
        for row in reader:
            name.append(row[0])
            password.append(row[1])
        nh_dict= {}    
        for i in range(0 , len(name)):
            nh_dict[password[i]]= name[i]
    #section 2: calculate hash of 1000 to 9999 and match with password
    i = 1000
    dict2 = {}
    while i < 10000:
        i = str(i)
        haash= hashlib.sha256((i).encode('utf-8')).hexdigest() 
        dict2[haash] = i
        i = int(i)
        i += 1    
    for k in nh_dict:
        if k in dict2:
            esm = nh_dict[k]
                #print (esm, ',' , i)
            file.write('%s,%s\n' %(esm , dict2[k]))         
    file.close()
    return
