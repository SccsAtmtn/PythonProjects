import sys,os
import numpy as np
import wave
from gmm import *
from sreutil import *
from mywave import *
from MFCC import *

def super_vector(test_file_name, ubm_file):
    wav = mywave()
    waveData = wav.WaveRead(test_file_name)
    waveVadIdx = vad(waveData ** 2)
    waveData = waveData[waveVadIdx]

    MFCC_obj = MFCC(40,12,300,3400,0.97,16000,50,0.0256,256)
    MFCC_coef = MFCC_obj.sig2s2mfc(waveData)

    ubm = GMM(n_mix = 128, n_dim = 12)
    ubm.read(ubm_file)
    ubm.adapt(MFCC_coef)

    return ubm.means

