# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:19:08 2016

@author: huangxinyuan
"""
import sys,os
import pickle
import numpy as np
import mywave
import math
from gmm import *
from MFCC import *

if __name__ == '__main__':
    print __doc__
    
    samprate = 16000
    length = 10*samprate
    
    ubms_dir = 'ubms'
    supervector_dir = 'supervector'
    if not os.path.exists(supervector_dir):
        os.mkdir(supervector_dir)
    
    train_data_dir = 'train_data'
    train_data = os.listdir(train_data_dir)
    
    wav = mywave.mywave()
    
    special = ['train_2013011050_mlh_M.wav','train_2013011055_huangyiqing_M.wav',
               'train_2013012061_huangxinyuan_M.wav']
    
    MFCC_obj = MFCC(40,12,300,3400,0.97,samprate,50,0.0256,256)
    dim = 12
    
    for train_wav in train_data:
        if train_wav == '.DS_Store':
            continue
        print train_wav
        if not os.path.exists(supervector_dir+r'/'+train_wav[6:16]):
            os.mkdir(supervector_dir+r'/'+train_wav[6:16])
        wave = wav.WaveRead(train_data_dir+r'/'+train_wav)
        piece_num = int(wave.shape[0]/length)
        print 'sum of piece:', piece_num
        temp = range(piece_num)
        for loop in temp:
            print 'piece:',loop+1
            beginp = loop*samprate
            endp = (loop+1)*samprate-1
            sig = wave[beginp:(endp+1)]
            MFCC_coef = MFCC_obj.sig2s2mfc(sig)
            
            #energy = np.ndarray(shape = (MFCC_coef.shape[0],1),dtype = 'float64')
            #energy[:,0] = 10*np.log10((MFCC_coef**2).sum(axis=1))
            #MFCC_coef = np.hstack((MFCC_coef,energy))
                       
            """
            dtm1 = np.ndarray(shape = MFCC_coef.shape,dtype = 'float64' )        
            dtm1[0:2,:] = 0;
            dtm1[MFCC_coef.shape[0]-2:MFCC_coef.shape[0],:] = 0;        
            for loop2 in range(2,MFCC_coef.shape[0]-2):
                dtm1[loop2,:] = -2*MFCC_coef[loop2-2,:]-MFCC_coef[loop2-1,:]+MFCC_coef[loop2+1,:]+2*MFCC_coef[loop2+2,:]
            dtm1 = dtm1/3;
            dtm2 = np.ndarray(shape = MFCC_coef.shape,dtype = 'float64' ) 
            dtm2[0:4,:] = 0
            dtm2[MFCC_coef.shape[0]-4:MFCC_coef.shape[0],:] = 0
            for loop2 in range(4,MFCC_coef.shape[0]-4):
                dtm2[loop2,:] = -2*dtm1[loop2-2,:]-dtm1[loop2-1,:]+dtm1[loop2+1,:]+2*dtm1[loop2+2,:]
            dtm2 = dtm2/3;
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
            adapted_gmm = GMM()
            adapted_gmm.read(ubms_dir+r'/ubm')
            #for loop2 in range(0,8):
                #adapted_gmm.adapt(MFCC_coef)
            adapted_gmm.adapt(MFCC_coef) #MAP Adaptation
            svector = adapted_gmm.means  #svector 即为这段10秒音频的超矢量
            pickle.dump(svector,open(supervector_dir+r'/'+train_wav[6:16]+r'/'+str(loop),'wb'))
    
    supervector_test_dir = 'supervector_test'
    if not os.path.exists(supervector_test_dir):
        os.mkdir(supervector_test_dir)
    test_data = os.listdir('test_data')
    for test_wave in test_data:
        if test_wave == '.DS_Store':
            continue
        print test_wave
        if not os.path.exists(supervector_test_dir+r'/'+test_wave[5:15]):
            os.mkdir(supervector_test_dir+r'/'+test_wave[5:15])
        wave = wav.WaveRead('test_data/'+test_wave)
        piece_num = int(wave.shape[0]/length)
        print 'sum of piece:', piece_num
        temp = range(piece_num)
        for loop in temp:
            print 'piece:',loop+1
            beginp = loop*samprate
            endp = (loop+1)*samprate-1
            sig = wave[beginp:(endp+1)]
            MFCC_coef = MFCC_obj.sig2s2mfc(sig)
            
            #energy = np.ndarray(shape = (MFCC_coef.shape[0],1),dtype = 'float64')
            #energy[:,0] = 10*np.log10((MFCC_coef**2).sum(axis=1))
            #MFCC_coef = np.hstack((MFCC_coef,energy))
            
            """
            dtm1 = np.ndarray(shape = MFCC_coef.shape,dtype = 'float64' )        
            dtm1[0:2,:] = 0;
            dtm1[MFCC_coef.shape[0]-2:MFCC_coef.shape[0],:] = 0;        
            for loop2 in range(2,MFCC_coef.shape[0]-2):
                dtm1[loop2,:] = -2*MFCC_coef[loop2-2,:]-MFCC_coef[loop2-1,:]+MFCC_coef[loop2+1,:]+2*MFCC_coef[loop2+2,:]
            dtm1 = dtm1/3;
            dtm2 = np.ndarray(shape = MFCC_coef.shape,dtype = 'float64' ) 
            dtm2[0:4,:] = 0
            dtm2[MFCC_coef.shape[0]-4:MFCC_coef.shape[0],:] = 0
            for loop2 in range(4,MFCC_coef.shape[0]-4):
                dtm2[loop2,:] = -2*dtm1[loop2-2,:]-dtm1[loop2-1,:]+dtm1[loop2+1,:]+2*dtm1[loop2+2,:]
            dtm2 = dtm2/3;
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
            MFCC_coef = (MFCC_coef-mean)/var#nn,b.ru
            """
            adapted_gmm = GMM()
            adapted_gmm.read(ubms_dir+r'/ubm')
            #for loop2 in range(0,8):           
                #adapted_gmm.adapt(MFCC_coef)
            adapted_gmm.adapt(MFCC_coef) #MAP Adaptation
            svector = adapted_gmm.means  #svector 即为这段10秒音频的超矢量
            pickle.dump(svector,open(supervector_test_dir+r'/'+test_wave[5:15]+r'/'+str(loop),'wb'))


