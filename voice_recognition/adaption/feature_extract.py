# -*- coding: utf-8 -*-
'''
brief:
This script extracts MFCC features from the training data

side effect:
MFCC features are saved in file features.txt
'''

import sys,os
from MFCC import *
import numpy as np
import pickle
import math
from mywave import *



if __name__ == '__main__':
    print __doc__

	#  extract features from UBM data
    ubm_dir = 'train_data_for_UBM'
    ubm_data_dirs = os.listdir(ubm_dir)
    dim = 12
    sig = np.array([])
    features_M = np.ndarray(shape = (0,dim), dtype = 'float64')
    features_F = np.ndarray(shape = (0,dim), dtype = 'float64')
    features = np.ndarray(shape = (0,dim), dtype = 'float64')
    wav = mywave()
    print 'hello'
    for ubm_data_dir in ubm_data_dirs:
        print 'hello'
        print ubm_data_dir
        if ubm_data_dir == '.DS_Store':
            continue			
        sig = wav.WaveRead(ubm_dir+r'/'+ubm_data_dir)
        MFCC_obj = MFCC(40,12,300,3400,0.97,16000,50,0.0256,256)
        MFCC_coef = MFCC_obj.sig2s2mfc(sig)
        #energy = np.ndarray(shape = (MFCC_coef.shape[0],1),dtype = 'float64')
        #energy[:,0] = 10*numpy.log10((MFCC_coef**2).sum(axis=1))
        #MFCC_coef = np.hstack((MFCC_coef,energy))
        """
        dtm1 = np.ndarray(shape = MFCC_coef.shape,dtype = 'float64' ) 
        #初始化dtm1
        dtm1[0:2,:] = 0
        dtm1[MFCC_coef.shape[0]-2:MFCC_coef.shape[0],:] = 0;  
        #计算dtm1
        for loop2 in range(2,MFCC_coef.shape[0]-2):
            dtm1[loop2,:] = -2*MFCC_coef[loop2-2,:]-MFCC_coef[loop2-1,:]+MFCC_coef[loop2+1,:]+2*MFCC_coef[loop2+2,:]
        dtm1 = dtm1/3;
        dtm2 = np.ndarray(shape = MFCC_coef.shape,dtype = 'float64' )
        #初始化dtm2
        dtm2[0:4,:] = 0
        dtm2[MFCC_coef.shape[0]-4:MFCC_coef.shape[0],:] = 0
        #计算dtm2
        for loop2 in range(4,MFCC_coef.shape[0]-4):
            dtm2[loop2,:] = -2*dtm1[loop2-2,:]-dtm1[loop2-1,:]+dtm1[loop2+1,:]+2*dtm1[loop2+2,:]
        dtm2 = dtm2/3;
        #拼接成39维向量，并去除前4个和最后4个向量
        MFCC_coef = np.hstack((MFCC_coef,dtm1,dtm2))
        MFCC_coef = MFCC_coef[4:MFCC_coef.shape[0]-4,:]
        """
        """
        mean = MFCC_coef.mean(axis=0)
        mean = mean.reshape([1,dim])
        mean = mean.repeat(MFCC_coef.shape[0],axis=0)
        var = MFCC_coef.var(axis=0)
        var = var.reshape([1,dim])
        var = var.repeat(MFCC_coef.shape[0],axis=0)
        MFCC_coef = (MFCC_coef-mean)/var
        """
        features = np.vstack((features,MFCC_coef))
        """
        if ubm_data_dir[-5] == 'M':
            features_M = np.vstack((features_M,MFCC_coef))
        elif ubm_data_dir[-5] == 'F':
            features_F = np.vstack((features_F,MFCC_coef))
        """
    pickle.dump([features,features_M,features_F],open(ubm_dir+r'_features.txt','wb'))
