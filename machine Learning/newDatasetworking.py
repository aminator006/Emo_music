# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:36:56 2017

@author: AJAY
"""

import numpy as np

import pandas as pd
import cv2

fishface = cv2.face.LBPHFaceRecognizer_create()

# Importing the dataset
dataset = pd.read_csv('fer2013.csv')
X = dataset.iloc[:,0].values
y = dataset.iloc[1,1]

i=0
for p in y:
    if(p==' '):
        i=i+1;

print(i)

training_label = []
training_data = []


for xx in X:
    training_label.append(xx)

for yy in y:
    training_data.append(yy)
    

fishface.train(np.asarray(training_data),np.asarray(training_label))