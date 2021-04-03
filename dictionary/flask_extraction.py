import itertools
import pandas as pd
import re
import csv
import openpyxl
from csv import reader
from collections import OrderedDict
def matrix_item():
    values=[]
    keylist=[]
    row=[]
    with open(path, mode='r') as infile:
        reader = csv.reader(infile)
        with open('coors_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]:rows[1] for rows in reader}
    # print(mydict)
    col_list = ["description"]
    df = pd.read_csv("NDC.csv", usecols=col_list)
    temp_lists = df.values.tolist()
    # print(temp_lists)
    for key,value in mydict.items():
        keylist.append(key)
    keylist.insert(0,'product Name')
    print(keylist)
    with open('matrix.csv', 'a',newline="") as csv_file:  
        writer = csv.writer(csv_file)
        writer.writerow(keylist)                                                                
    for item in temp_lists:
        
        for j in item:
            print("DESC: ",j)
            trow=[]  
            trow.append(j) 
            for key,value in mydict.items():
                
                # print(key,value)
                val = value.split(",")
                # print(val)
                for v in val:
                    
                    if re.findall(r"\b"+re.escape(v)+r"\b", j):
                        for i in range(0,len(keylist)):
                            if(i == keylist.index(key)):
                                if(trow[i]):
                                    trow[i]=trow[i]+"//"+v
                                else:
                                    trow.insert(i,v)
                            else:
                                trow.append("")
                        # print(trow)
            with open('matrix.csv', 'a',newline="" ) as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(trow)

matrix_item('C:\Users\Lenovo\Desktop\dictionary\NDC.csv')