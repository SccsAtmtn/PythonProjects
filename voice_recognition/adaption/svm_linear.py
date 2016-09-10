# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 22:30:27 2016

@author: huangxinyuan
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys,os
import numpy as np
import pickle
import mywave
from gmm import *
from MFCC import *

manu = os.listdir('C:\Users\yqRubick\Desktop\proj\supervector') 
vect_to_store = []

#生成trkernel
mix = 128
dim = 12
gmm = GMM()
gmm.read('C:\Users\yqRubick\Desktop\proj\ubms\ubm')
icovs = gmm.icovs
weights = gmm.weights
kernel = np.ndarray(shape = (mix,dim), dtype = 'float64')
for loop in range(0,128):
    kernel[loop,:] = (weights[loop]**0.5)*(icovs[loop,:]**0.5)
trkernel = []
for loop in range(0,128):
    trkernel = np.append(trkernel,kernel[(loop-1)*dim:loop*dim])

count = 0
for i in manu:
    if i == '.DS_Store':
        continue
    count = count+1
    f = os.listdir('C:\Users\yqRubick\Desktop\proj\supervector\\'+i)
    for index in f:
        svector = pickle.load(open('C:\Users\yqRubick\Desktop\proj\supervector\\'+i+r'/'+index,'rb'))
        tempp = []
        for k in range(0,128):
            tempp = np.append(tempp,svector[(k-1)*dim:k*dim])
        
        temp = tempp
        newvect = {}
        for k in range(0,dim*mix):
            newvect[k+1]=temp[k]
        new = [count,newvect]

        vect_to_store.append(new)
#pickle.dump(vect_to_store,open('svm_data_kernel','wb'))
        
count = 0
manu_test = os.listdir('C:\Users\yqRubick\Desktop\proj\supervector_test')
vect_to_store_test = []
for i in manu_test:#range(1,len(manu_test)):
    if i == '.DS_Store':
        continue
    count = count+1
    f = os.listdir('C:\Users\yqRubick\Desktop\proj\supervector_test\\'+i)
    
    for index in f:
        svector = pickle.load(open('C:\Users\yqRubick\Desktop\proj\supervector_test\\'+i+r'/'+index,'rb'))
        tempp = []
        for k in range(0,128):
            tempp = np.append(tempp,svector[(k-1)*dim:k*dim])
        
        temp = tempp
        newvect = {}
        for k in range(0,dim*mix):
            newvect[k+1] = temp[k]
        new = [count,newvect]
 
        vect_to_store_test.append(new)
#pickle.dump(vect_to_store_test,open('svm_data_fortest_kernel','wb'))
        
os.chdir('C:\Users\yqRubick\Desktop\proj\libsvm-3.21\python')
from svmutil import *

x = []
y = []

for i in range(0,np.size(vect_to_store)/2):
   y.append(vect_to_store[i][0])
   x.append(vect_to_store[i][1])
'''
x_t = []
y_t = []

for i in range(0,np.size(vect_to_store_test)/2):
   y_t.append(vect_to_store_test[i][0])
   x_t.append(vect_to_store_test[i][1])

m = svm_train(y,x,'-t 0 -c 19.5')

p_lable , p_acc , p_val = svm_predict(y_t,x_t,m)
svm_save_model('C:\Users\yqRubick\Desktop\proj\predict_linear.model',m)
'''