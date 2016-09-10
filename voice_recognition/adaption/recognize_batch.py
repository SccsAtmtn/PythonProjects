import sys,os
import numpy as np
import pickle
from gmm import *
from SuperVector import *

sys.path.append(r'D:\Python Projects\voice_recognition\libsvm-3.21\python') #运行时需修改该路径为libsvm文件夹下python文件夹的绝对路径
from svmutil import *


def recognize_batch(path):
    '''
    运行时需要修改以下三个变量为相应文件在当前系统中的绝对路径
    ubm_path = ubm文件的绝对路径
    model_path = svm模型文件的绝对路径
    manu_path = manu文件的绝对路径
    '''
    ubm_path = r'D:\Python Projects\voice_recognition\ubms\ubm'
    model_path = r'D:\Python Projects\voice_recognition\predict_kernel.model'
    manu_path = r'D:\Python Projects\voice_recognition\manu'

    ground_truth = path[len(path)-10:len(path)]


    mix = 128
    dim = 12

    gmm = GMM()
    gmm.read(ubm_path)

    icovs = gmm.icovs
    weights = gmm.weights
    kernel = np.ndarray(shape = (mix,dim), dtype = 'float64')
    for loop in range(0,128):
        kernel[loop,:] = (weights[loop]**0.5)*(icovs[loop,:]**0.5)
    trkernel = []
    for loop in range(0,128):
        trkernel = np.append(trkernel,kernel[(loop-1)*dim:loop*dim])
     
    newpath = os.listdir(path)


    manu = pickle.load(open(manu_path,'rb'))
    m = svm_load_model(model_path)


    count = 0
    correct = 0

    for i in newpath:
        count = count + 1
        sv = super_vector(path+'\\'+i,ubm_path)
         
        tempp = []
        for k in range(0,128):
            tempp = np.append(tempp,sv[(k-1)*dim:k*dim])
        temp = tempp*trkernel
        
        newvect = {}
        for k in range(0,dim*mix):
            newvect[k+1] = temp[k]
        new = [1,newvect]
        
        x = []
        y = []
        x.append(new[1])
        y.append(new[0])
        

        p_lable , p_acc , p_val = svm_predict(y,x,m)
      
        name = manu[int(p_lable[0])-1]
        
        if(name == ground_truth):
            correct = correct + 1

    acc = float(correct)/float(count)*100   
    return acc
