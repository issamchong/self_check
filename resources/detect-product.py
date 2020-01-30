

import cv2
import matplotlib.pyplot as plt
import numpy as np


# these are gloabal define once 
  
windowname = "live"
cv2.namedWindow(windowname)
cap = cv2.VideoCapture('udp://admin:admin@192.168.0.12/videostream.cgi?user=admin&pwd=admin&resolution=32&rate=0 ')
#path='C:\\Users\\6530\\Google Drive\\Embeded vision\\City mall\\cashier fraud\\front.jpg'

#img=cv2.imread(path,0)
#gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #image1= np.int32(img)

    #img2= cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    #cv2.imshow("image",img2)
    #cv2.imshow("test",sub)
CASCADE_FILE = '/home/issam/detectionProduct/resources/classifier/cascade.xml'

cascade = cv2.CascadeClassifier(CASCADE_FILE)
j=0
while cap.isOpened():
        
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  rectangles = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,
  minSize=(40, 40),maxSize=(80,80))
  detection =list(enumerate(rectangles)) 
  #print(rectangles)
  if len(detection)>0:
     x=0
     y=0
     w=0  
     h=0   
     for i in range(len(detection)): 
      data=detection[i]
      dimen=data[1] 
      x1=dimen[0]
      y1=dimen[1]
      w=dimen[2]
      h=dimen[3]
      x2=x1+w               
      y2=y1+h   
      cv2.rectangle(frame, (x1,y1), (x2 , y2), (0, 0, 200 ), 3)
      j=j+1
      if j==1:
       p1=(x1,y1)
      if j>1:
       print(j)     
       p2=(x1,y1)
       print(p2,p1)
       if p1[0]-p2[0] >10:
        #cv2.line(frame, p1, p2, (0,0,255), 3)
        j=0
       cv2.line(frame, p1, p2, (0,0,255), 3)
 
  #frame=cv2.resize(frame,(640,480),interpolation=cv2.INTER_AREA)
  #gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #mask=cv2.inRange(hsv,low, high)
  #frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  #diff=cv2.absdiff(frame,frame1)
  #_,final=cv2.threshold(diff,25,255,cv2.THRESH_BINARY) 
        #cv2.imshow("mask",mask)
        #cv2.imshow("blue_mask",blue)
       # print(mask)cv
  #cv2.imshow("test1",frame1)
  #cv2.imshow("test2",frame)
  cv2.imshow("test",frame)
  if cv2.waitKey(30) == 27:
      break 
        
cv2.destroyAllWindows()
cap.release()
    
         
