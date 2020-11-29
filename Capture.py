# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:16:28 2020

@author: Guney Doruk
"""

import cv2 

directory = r'C:\Captured images'
 
video_capture = cv2.VideoCapture(0) 

success = video_capture.isOpened()

if(success == False):
    video_capture.open(0)
    success = True
    
i = 0
fps = video_capture.get(cv2.CAP_PROP_FPS)
print(fps)

while success: 
       
    ret, frame = video_capture.read() 
  
    cv2.imshow('frame', frame) 
      
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
    if cv2.waitKey(100) & 0xFF == ord('f'): 
        name = "\deneme_"+str(i)+ ".jpeg"
        path = directory + name
        cv2.imwrite(path,frame)
        i += 1
        
        

video_capture.release() 
 
cv2.destroyAllWindows() 
