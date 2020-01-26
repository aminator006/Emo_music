# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 01:32:53 2017

@author: AJAY
"""

import cv2
print(cv2.__version__)
import glob
import random
import numpy as np

emotions = ["anger", "sadness", "happy"] #Emotion list
fishface = cv2.face.LBPHFaceRecognizer_create()#Initialize fisher face classifie

data = {}
picdata = []

def get_files(emotion): #Define function to get file list, randomly shuffle it and split 80/20
    files = glob.glob("dataset\\%s\\*" %emotion)
    random.shuffle(files)
    training = files[:int(len(files)*1)] #get first 80% of file list
    #prediction = files[-int(len(files)*0.2):] #get last 20% of file list
    return training

def make_sets():
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []
    for emotion in emotions:
        training = get_files(emotion)
        #Append data to training and prediction list, and generate labels 0-7
        for item in training:
            image = cv2.imread(item) #open image
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale
            training_data.append(gray) #append image array to training data list
            training_labels.append(emotions.index(emotion))
    
    extra_files = glob.glob("pictures\\*")
    prediction = extra_files[-int(len(extra_files)*1):] 
    
    i=0;
    for item in prediction: #repeat above process for prediction set
        print('welcome')
        image = cv2.imread(item)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print('lenght of gray :')
        print(len(gray))
        picdata=gray
        prediction_data.append(gray)        
        prediction_labels.append(i)
        i=i+1

    return training_data, training_labels, prediction_data, prediction_labels



def call_predict():
    training_data, training_labels, prediction_data, prediction_labels = make_sets()
    print("training fisher face classifier")
    print("size of training set is:", len(training_labels), "images")
    fishface.train(training_data, np.asarray(training_labels))
    cnt=0;
    for image in prediction_data:
        print(image)
        pred,conf = fishface.predict(image)
        print(pred)
        print(emotions[pred])
        print(conf)
