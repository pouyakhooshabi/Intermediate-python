import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    #section 1: input file and break it to name and password
    with open(input_file_name , newline='') as f:
        reader = csv.reader(f)
        file = open(output_file_name ,"w")
        name= []
        password=[]
        for row in reader:
            name.append(row[0])
            password.append(row[1])
        nh_dict= {}    
        i = 0
        while i < 2:
            nh_dict[password[i]]= name[i]
            i += 1
    #section 2: calculate hash of 1000 to 9999 and match with password
    i = 1000
    while i < 10000:
        i = str(i)
        haash= hashlib.sha256((i).encode('utf-8')).hexdigest() 
        j= 0
        for k in password:
            if haash == k:
                esm = nh_dict[k]
                #print (esm, ',' , i)
                file.write('%s,%s \n' %(esm , i)))
        i = int(i)
        i += 1            
    file.close() 
    return

