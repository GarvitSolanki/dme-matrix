import itertools
import pandas as pd
import re
import csv
import openpyxl
from csv import reader
from collections import OrderedDict
values=[]
keylist=[]
row=[]
with open('Balloon.csv', mode='r') as infile:
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
    print(item)
    for j in item:
        # with open('matrix.csv', 'a') as csv_file:
        #     writer = csv.writer(csv_file) 
        #     writer.writerow([j])
        print("desc:",j)
        trow=[]  
        trow.append(j) 
        for key,value in mydict.items():
            
            # print(key,value)
            val = value.split(",")
            # print(val)
            for v in val:
                
                if re.findall(r"\b"+re.escape(v)+r"\b", j):
                    # print("KEY: ",key," VALUE: ",v)
                    # print(keylist.index(key),key,v)
                    for i in range(0,len(keylist)):
                        if(i == keylist.index(key)):
                            if(trow[i]):
                                trow[i]=trow[i]+"//"+v
                            else:
                                trow.insert(i,v)
                        else:
                            trow.append("")
                    # print(trow)
        with open('matrix.csv', 'a',newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(trow)

                        # writer.writerow([key,v])
                    # myworkbook=openpyxl.load_workbook("matrix.xlsx")
                    # worksheet= myworkbook.get_sheet_by_name('matrix')
                    # for i in range(1,38):
                    #     cell=worksheet.cell(row=row+1, column=i)
                    #     cell.value=v
                    
                        
                        


                        
                        
                        
        
                    # if(v==k):
                    #     print(v)
                    #     found_word+=1
                # if (' ' + v + ' ' ) in (' ' + j + ' '):
                #     print(key,v)
            # if found_word == len(v):
            #     print(len(v))
            
                    

                # check = j.find(v)
                # print(check)
                # if(check != -1):
                #     print(v)
                
        
        
    # #    print(item[0])
    # for key, value in mydict.items():
    #     val = value.split()
    #     # print(val)
    #     if any(v in item[0] for v in val):
    #         print(v)
    # # for j in item:
    # #     x=j.split()
    # #     # print(x)
    # #     for k in x:
    # #         for value in mydict.values():
    # #             if value in k:
    # #                 print(k)
             








 
                
                    



