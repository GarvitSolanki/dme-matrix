from flask import Flask
import flask
from flask import jsonify
from flask import json
from flask import Flask, render_template, request, redirect, url_for, session,Response,json
from flask_cors import CORS
from flask_api import FlaskAPI
import itertools
import pandas as pd
import re
import sys
import csv
import pandas as pd
import re
import csv
import uuid
import openpyxl
from csv import reader
from collections import OrderedDict


app = Flask(__name__)

CORS(app)

@app.route('/matrix_item_logic', methods=['GET'])
def extract():
    obj1 = flask.request.json
    # obj1=json.loads(str1)
    # dummy = json.dumps(obj1)
    identity=uuid.uuid1()
    baseurl="C:/Users/Lenovo/Desktop/dictionary"
    name=baseurl+"\matrix"+str(identity)+".csv"
    print(name)
    values=[]
    keylist=[]
    trow=[] 
    try:
        with open('Balloon.csv', mode='r') as infile:
            reader = csv.reader(infile)
            with open('coors_new.csv', mode='w') as outfile:        
                writer = csv.writer(outfile)
                mydict = {rows[0]:rows[1] for rows in reader}
                print(mydict)
    except:
        return("Error 404: couldnt find the dictionary files")
    try:
        col=obj1['desc']
        # print(col)
        path=obj1['path']
        # print(path)
        df = pd.read_csv(path,usecols=[col]) 
    except:
        return("Error 404: couldnt find the input files")
    try:
        temp_lists = df.values.tolist()
        for key,value in mydict.items():
            keylist.append(key)
        keylist.insert(0,'product Name')
        print(len(keylist))
        with open(name, 'w') as csv_file:  
            writer = csv.writer(csv_file)
            writer.writerow(keylist)
        # print(temp_lists)
    
        for item in temp_lists:

            # print(item)
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
                with open(name, 'a', newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(trow)

                    


        update={
            'status':'200', 
            'msg':'processed successfully',
            'filename':'matrix.csv',
            'path':'C//Users//Lenovo//Desktop//dictionary//matrix.csv'
            }
        return jsonify(update)
    except:
        return("Error 500:server Error")
        
if __name__ == '__main__':
            app.run(debug=True)