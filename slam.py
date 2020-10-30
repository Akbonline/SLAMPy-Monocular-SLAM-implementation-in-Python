import numpy as np
import cv2
import os,sys,time,g2o

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("%s takes in .mp4 as an arg" %sys.argv[0])
        exit(-1)
    cap = cv2.VideoCapture(sys.argv[1]) # Can try Realtime(highly unlikely though)
    while cap.isOpened():
        ret, frame = cap.read()
        frame1 = cv2.resize(frame, (720,400)) #Resizing the original window
        if ret == True:
          cv2.imshow("Frame",frame1)    
          if cv2.waitKey(1) & 0xFF == ord('q'):   #Quit Condition
              break
        else:
          break
    cap.release() 
    cv2.destoryAllWindows()

