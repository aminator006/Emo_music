# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:04:19 2017

@author: AJAY
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import json


Emotions = ['fear','contempt','anger','sadness','surprise','neutral','disgust','happiness']


def predict():
    headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'dc5a9336dc024bc69d4a4d49b481be47',
    }

    params = urllib.parse.urlencode({
            })

    # Replace the example URL below with the URL of the image you want to analyze.
    body = "{ 'url': 'http://www.freepngimg.com/download/happy_person/2-2-happy-person-free-download-png.png' }"

    try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
    #   URL below with "westcentralus".
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        my_json = data.decode('utf8')
        data = json.loads(my_json)    
        maxval = 0
        emotionfound = ""
        for emotion in Emotions:
            if maxval < data[0]['scores'][emotion]:
                maxval = data[0]['scores'][emotion]
                emotionfound = emotion  
        print(emotionfound)
        conn.close()
    except Exception as e:
            print(e.args)

predict()