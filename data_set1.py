#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 05:31:53 2017

@author: abhilasha
"""

import csv
import os
#import random
from sklearn import tree
x=[]
arr=[0,1]
y=[]
z=[]
connection_result=[]
Connection_info=dict()
with open('Desktop/test1.csv','r') as tcpfile:
    reader=csv.reader(tcpfile,delimiter=',')
    
    for row in reader:
        y.append(row[5])
        del row[5]
        if row[0] in Connection_info:
            row[0]=Connection_info[row[0]]
        else:
            newer={row[0]:len(Connection_info)}
            Connection_info.update(newer)
            row[0]=Connection_info[row[0]]#for protocols in Connection_info:
        temp=row[3].split('.')
        y1=temp[0]+'.'+temp[1]
        y2=temp[2]+'.'+temp[3]
        temp[0]=y1
        temp[1]=y2
        temp2=row[4].split('.')
        y1=temp2[0]+'.'+temp2[1]
        y2=temp2[2]+'.'+temp2[3]
        temp2[0]=y1
        temp2[1]=y2
        row.pop(3)
        row.pop(3)
        row.insert(3,temp[0])
        row.insert(4,temp[1])
        row.insert(5,temp2[0])
        row.insert(6,temp2[1])
        x.append(row)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
with open('tcpdump.csv','r') as testfile:
    reader=csv.reader(testfile,delimiter=',')
    for row in reader:
        if row[0] in Connection_info:
            row[0]=Connection_info[row[0]]
        else:
            newer={row[0]:len(Connection_info)}
            Connection_info.update(newer)
            row[0]=Connection_info[row[0]]#for protocols in Connection_info:
        temp=row[3].split('.')
        y1=temp[0]+'.'+temp[1]
        y2=temp[2]+'.'+temp[3]
        temp[0]=y1
        temp[1]=y2
        temp2=row[4].split('.')
        y1=temp2[0]+'.'+temp2[1]
        y2=temp2[2]+'.'+temp2[3]
        temp2[0]=y1
        temp2[1]=y2
        row.pop(3)
        row.pop(3)
        row.insert(3,temp[0])
        row.insert(4,temp[1])
        row.insert(5,temp2[0])
        row.insert(6,temp2[1])
        z.append(row)

col=[]
#print(connection_result)
#os.system("rm interpretation.csv")
with open('Desktop/interpretation7.csv','w+') as output:
    writer=csv.writer(output,delimiter='\n')
    for row in clf.predict(z):#and col in output:
       #new_row=[col + ',' + row]
       #output.seek(0)
       writer.writerow(row)
print(clf.predict(z))
#print(type(connection_result))
dot_data = tree.export_graphviz(clf, out_file="tree.dot")
#graph = pydotplus.graph_from_dot_data(dot_data)  
os.system("dot -Tpng tree.dot -o Desktop/tree7.png")

        


       
        

        
"""print (y)
print (x)
print (Connection_info)"""