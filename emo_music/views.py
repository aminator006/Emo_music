from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ProfilePic
from django.shortcuts import render

class TestPage(LoginRequiredMixin,TemplateView):
    template_name = 'test.html'
    print('hello testpage')

    def get(self, request, *args, **kwargs):
        flag = False
        photoobject = ''
        for ob in ProfilePic.objects.all():
            if request.user.username == ob.name.username:
                flag = True
                photoobject = ob

        return render(request,'test.html',{'allprophoto': photoobject,'flag':flag})


class ThanksPage(TemplateView):
    template_name = 'thanks.html'



class HomePage(TemplateView):
    template_name = "index.html"


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        else :
            return HttpResponseRedirect(reverse("login"))
        return super().get(request, *args, **kwargs)


from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings

@csrf_exempt
def save_image(request):
    if request.body:
        f = open(settings.MEDIA_ROOT + '/webcamimages/someimage.jpeg','wb')
        f.write(request.body)
        f.close()
        print('something found')
        return HttpResponse('http://127.0.0.1:8000/media/webcamimages/someimage.jpeg')
    else:
        print('not get any data.')
        return HttpResponse('no data')




import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import json
from musicapp import views
from musicapp.models import Song
import shutil
import random
import string



import cv2
print(cv2.__version__)
import glob
import random
import numpy as np

SIZE_FACE=48
EMOTIONS = ['angry', 'happy', 'sad','neutral']#emotion list
fishface = cv2.face.LBPHFaceRecognizer_create()#Initialize fisher face classifier

data = {}

def get_data(): #Define function to get file list, randomly shuffle it and split 80/20
    images=np.load('data_train.npy')
    labels= np.load('labels_train.npy')
    print(length(labels))
    images_test = np.load('data_test.npy')
    images_test = images_test[:300]
    labels_test = np.load('labels_test.npy')
    print(labels_test)
    labels_test = labels_test[:300]
    images=images.reshape([-1, SIZE_FACE, SIZE_FACE, 1])
    images_test = images_test.reshape([-1, SIZE_FACE, SIZE_FACE, 1])
    # return images,labels,images_test,labels_test


def run_recognizer():
    training_data, training_labels, prediction_data, prediction_labels = get_data()

    print("training fisher face classifier")
    print("size of training set is:", len(training_labels), "images")
    fishface.train(training_data, np.asarray(training_labels))
    print("predicting classification set: ",len(prediction_labels))
    cnt = 0
    correct = 0
    incorrect = 0
    for image in prediction_data:
        pred, conf = fishface.predict(image)
        print(EMOTIONS[pred])
        if pred == prediction_labels[cnt]:
            correct += 1
            cnt += 1
        else:
            incorrect += 1
            cnt += 1
    return ((100*correct)/(correct + incorrect))

#Now run it
metascore = []
correct=0
for i in range(0,1):
    # correct = run_recognizer()
    print("got", correct, "percent correct!")
    metascore.append(correct)

print("\n\nend score:", np.mean(metascore), "percent correct!")



def EmotionTemp(request):
    songList = Song.objects.all()

    print('hello')
    headers = {
       
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'dc5a9336dc024bc69d4a4d49b481be47',
    }
    params = urllib.parse.urlencode({
    })
    ImageInBinary = ''
    pathtoImage = settings.MEDIA_ROOT + '/webcamimages/someimage.jpeg'
    with open(pathtoImage, "rb") as imageFile:
        f = imageFile.read()
        ImageInBinary = bytearray(f)

    
    body = ImageInBinary
    emotionfound = 'happiness'
    Songindex = 1
    Emotions = ['anger','sadness','neutral','happiness']
    try:
       
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        my_json = data.decode('utf8')
        data = json.loads(my_json)
        # print(data)
        maxval = 0
        for emotion in Emotions:

            val = data[0]['scores'][emotion]
            print(val)
            if emotion == 'anger':
                    val = val * 4
            if emotion == 'sadness':
                    val = val * 4
            print(emotion)
            print(val)
            if maxval < val:
                maxval = val
                emotionfound = emotion

        print(emotionfound)
        str = ''
        str = str.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        shutil.copy(settings.MEDIA_ROOT + '/webcamimages/someimage.jpeg', settings.MEDIA_ROOT + '/webcamimages/'+emotionfound + str+'.jpeg')
        print('Image created successfully')
        conn.close()
        # copy an image in Database so that

    except Exception as e:
        print(e.args)

    return render(request,'emotion.html',{'emotionFoundtag':emotionfound,'songlist':songList,'Songindex': Songindex})
