#Submitted by Himanshu Doi for Screening Test of Busigence (Sagar Helped)
#Davies Bouldin Index Calculation

import os as os
os.chdir("C:\Users\Lenovo\Desktop\New folder")
import pandas as pd
import numpy as np
from numpy import linalg as LA
from scipy.spatial import distance
from sklearn.cluster import  k_means

df = pd.read_csv("Round1_Problem2-of-3_Dataset.csv")
df = df.dropna()
X1 = df.copy()
del X1['Customer']
del X1['Effective To Date']
X4=pd.get_dummies(X1)


n=10
clf=k_means(X4,n_clusters=n)
centroid=clf[0]
labels=clf[1]

c=[]
for i in range(0,n):
    c.append(LA.norm(centroid[i]))

d=np.zeros((n,n))
for i in range(0,n):
    for j in range(0,n):
        d[i][j]=distance.euclidean(centroid[i],centroid[j])

sumd=[]
for i in range(0,n):
    sumd.append(np.sum(d[i]))
    
s=[]
for i in range(0,n):
    s.append(sumd[i]/c[i])

R=np.zeros((n,n))
for i in range(0,n):
    for j in range(0,n):
        if(i!=j):R[i][j]=(s[i]+s[j])/d[i][j]
        else: R[i][j] = 0 

R1=[]

for i in range(0,n): R1.append(np.max(R[i]))  



a = np.sum(R1)

DB = a/n

print DB

     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
