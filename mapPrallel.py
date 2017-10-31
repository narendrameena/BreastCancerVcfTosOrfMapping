#@author narumeena
#@description map chromosome location in parallel


import csv
import pandas as pd
import multiprocessing 



#print('...'*20)
Genefile='data/SH.csv'
df1 = pd.read_csv(Genefile, delimiter = ',')
#print(len(df1))
#for k in range(263):
mutfiles = 'data/WGS.csv'
df2 = pd.read_csv(mutfiles)
#print(len(df2))
ss=list(df1.columns)
sd=list(df2.columns)
sds=ss+sd 
#print("columns \n ")
#print(sds)



#internal loop
def mapAll(i):
    kk = 0
    mm=0
    for j in range(i,len(df2.index)):
        with open("data/mapPrallell000.csv",'a') as gh:
            writer= csv.writer(gh)
           # kk = 0
            #file = open('Final_1.csv','a',newline='')
 #           print("line1 \n")
 #           print(df1.iloc[i,3])
 #           print("line 2 \n")
 #           print(df2.iloc[j,26])
            if str(df1.iloc[i,3]) == str(df2.iloc[j,26]):
                if int(df1.iloc[i,4])<= int(df2.iloc[j,27]) and int(df1.iloc[i,5])>= int(df2.iloc[j,28]):
                    #print((df1.iloc[i,3]), int(df2.iloc[j,26]))
                   
           
                    list1 = list(df1.iloc[i])+list(df2.iloc[j])
                   
                    if kk == 0:
                        #writer.writerow(sds)
                        kk = 1
 #                       print(list1)
                        writer.writerow(list1)

                    #file.write('Gene on chromosome '+str(df1.iloc[i,3])+' starts at '+str(int(df1.iloc[i,4]))+' ends at '+ str(int(df1.iloc[i,5]))+' and has mutation from '+str(int(df2.iloc[j,27]))+str(int(df2.iloc[j,28]))+'\n')
                    #print('Gene on chromosome',int(df1.iloc[i,1]),'starts at',(df1.iloc[i,2]),'ends at', int(df1.iloc[i,3]), 'and has mutation from', int(df2.iloc[j,28]),int(df2.iloc[j,29]))
    
                    else:
                        if int(df1.iloc[i,4])-200<= int(df2.iloc[j,27]) and int(df1.iloc[i,5])+200>= int(df2.iloc[j,28]):
                            list3 = list(df1.iloc[i])+list(df2.iloc[j])
                            
  #                          print(list3)
                            writer.writerow(list3)
                                
                        

pool = multiprocessing.Pool(64)
final= zip(*pool.map(mapAll, range(0, len(df1))))
print(final)