
# coding: utf-8

# In[106]:
#import libraries
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline
import cv2
from urllib.request import urlretrieve
from pylab import rcParams
class detecting_faces():
    def __init__(self,image_url,image_name):
        self.image_url=image_url
        self.image_name=image_name
        urlretrieve(self.image_url,self.image_name)
        self.image_object=cv2.imread(self.image_name)
        self.image_process()
        self.Face_Detector()
        self.eye_detector()
        
    def image_process(self):
        image=self.image_object
        self.processed_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.plot_image(self.processed_image,'preprocessed image')
    def plot_image(self,image,title):
        rcParams['figure.figsize']=8,6
        fig=plt.imshow(image,cmap='gray')
        plt.title(title)
        plt.axis('off')
        plt.show()
        
    def Face_Detector(self):
        self.haarcascade_url='https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
        self.haarcascade_name='haarcascade_frontalface_default.xml'
        urlretrieve(self.haarcascade_url,self.haarcascade_name)
        image_detect=cv2.CascadeClassifier(self.haarcascade_name)
        faces_list=image_detect.detectMultiScale(self.processed_image)
        for faces in faces_list:
            (x,y,w,h)=faces
            cv2.rectangle(self.processed_image,(x,y),(x+w,y+h),(0,255,0),(3))
        self.plot_image(self.processed_image,'Face_ Detector: post_processed_image')    
    def eye_detector(self)    :
        self.haarcascade_url='https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml'
        self.haarcascade_name='haarcascade_eye.xml'
        urlretrieve(self.haarcascade_url,self.haarcascade_name)
        eye_detect=cv2.CascadeClassifier(self.haarcascade_name)
        eyes_list=eye_detect.detectMultiScale(self.processed_image)
        print(eyes_list)
        for eyes in eyes_list:
            (ex,ey,ew,eh)=eyes
            cv2.rectangle(self.processed_image,(ex,ey),(np.int(ex+ew),np.int(ey+eh)),(0,25,0),(6))
        self.plot_image(self.processed_image,'Eye Detector: post_processed_image')    

