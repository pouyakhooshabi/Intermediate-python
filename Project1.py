import csv
import statistics
import collections
# For the average
from statistics import mean 
#Task1
def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name , newline='') as f:
        reader = csv.reader(f)
        file = open(output_file_name ,"w")
        for row in reader:
            name = row[0]
            data=[]
            for grades in row[1:]:
                data.append(float(grades))
            file.write('%s,%s \n' %(name , str(statistics.mean(data))))
        file.close()        
    return
#Task2    
def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name , newline='') as f:
        reader = csv.reader(f)
        file = open(output_file_name ,"w")
        our_dict= {}
        new_dict= {}
        for row in reader:
            name = row[0]
            data=[]
            for grades in row[1:]:
                data.append(float(grades))
            a= statistics.mean(data)
            if name not in our_dict:
                our_dict[name]= a
    new_dict= collections.OrderedDict(sorted(our_dict.items(), key=lambda t: t[1]))        
    for i in new_dict:
        file.write('%s,%s\n' %(i,new_dict[i]))            
    file.close()
    return
#task3
def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name , newline='') as f:
        reader = csv.reader(f)
        file = open(output_file_name ,"w")
        our_dict= {}
        new_dict= {}
        for row in reader:
            name = row[0]
            data=[]
            for grades in row[1:]:
                data.append(float(grades))
            a= statistics.mean(data)
            if name not in our_dict:
                our_dict[name]= a
    new_dict= collections.OrderedDict(sorted(our_dict.items(), key=lambda t: t[1], reverse=True))
    k = 0         
    for i in new_dict:
        if k<3:
            file.write(' %s,%s\n' %(i , str(new_dict[i])))
        k += 1
    file.close()
    return
#task4
def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name , newline='') as f:
        reader = csv.reader(f)
        file = open(output_file_name ,"w")
        our_dict= {}
        new_dict= {}
        for row in reader:
            name = row[0]
            data=[]
            for grades in row[1:]:
                data.append(float(grades))
            a= statistics.mean(data)
            if name not in our_dict:
                our_dict[name]= a
    new_dict= collections.OrderedDict(sorted(our_dict.items(), key=lambda t: t[1],))
    k = 0         
    for i in new_dict:
        if k<3:
            file.write('%f\n' %new_dict[i])
        k += 1            
    file.close()
    return
#task5
def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name , newline='') as f:
        reader = csv.reader(f)
        file = open(output_file_name ,"w")
        average_dict = []
        for row in reader:
            data=[]
            for grades in row[1:]:
                data.append(float(grades))
            average_dict.append(float(statistics.mean(data)))
    file.write(str(statistics.mean(average_dict)))
    file.close()
    return
