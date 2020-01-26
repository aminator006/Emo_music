usiimport cv2
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
    images_test = np.load('data_test.npy')
    labels_test = np.load('labels_test.npy')
    images=images.reshape([-1, SIZE_FACE, SIZE_FACE, 1])
    images_test = images_test.reshape([-1, SIZE_FACE, SIZE_FACE, 1])
    return images,labels,images_test,labels_test



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
for i in range(0,1):
    correct = run_recognizer()
    print("got", correct, "percent correct!")
    metascore.append(correct)

print("\n\nend score:", np.mean(metascore), "percent correct!")


