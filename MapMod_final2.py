# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:23:01 2017

@author: Arkajyoti Ghoshal
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:40:21 2017

@author: Arkajyoti Ghoshal
"""
import csv
print('...'*20)
Genefile='SH.csv'
import pandas as pd

df1 = pd.read_csv(Genefile, delimiter = ',')

#for k in range(263):
mutfiles = 'WGS.csv'
df2 = pd.read_csv(mutfiles)
ss=list(df1.columns)
sd=list(df2.columns)
sds=ss+sd
#print(sds)
kk = 0
mm=0
for i in range(len(df1.index)):
    for j in range(i,len(df2.index)):
        with open("Final000.csv",'a', newline = '') as gh:
            writer= csv.writer(gh)
           # kk = 0
            #file = open('Final_1.csv','a',newline='')
            if str(df1.iloc[i,3]) == str(df2.iloc[j,26]):
                if int(df1.iloc[i,4])<= int(df2.iloc[j,27]) and int(df1.iloc[i,5])>= int(df2.iloc[j,28]):
                    #print((df1.iloc[i,3]), int(df2.iloc[j,26]))
                   
           
                    list1 = list(df1.iloc[i])+list(df2.iloc[j])
                   
                    if kk == 0:
                        writer.writerow(sds)
                        kk = 1
                
                        writer.writerow(list1)

                    #file.write('Gene on chromosome '+str(df1.iloc[i,3])+' starts at '+str(int(df1.iloc[i,4]))+' ends at '+ str(int(df1.iloc[i,5]))+' and has mutation from '+str(int(df2.iloc[j,27]))+str(int(df2.iloc[j,28]))+'\n')
                    #print('Gene on chromosome',int(df1.iloc[i,1]),'starts at',(df1.iloc[i,2]),'ends at', int(df1.iloc[i,3]), 'and has mutation from', int(df2.iloc[j,28]),int(df2.iloc[j,29]))
    
                    else:
                        if int(df1.iloc[i,4])-200<= int(df2.iloc[j,27]) and int(df1.iloc[i,5])+200>= int(df2.iloc[j,28]):
                            list3 = list(df1.iloc[i])+list(df2.iloc[j])
                            
                
                            writer.writerow(list3)
                                
                        