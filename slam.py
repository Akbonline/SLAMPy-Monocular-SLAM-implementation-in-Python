import numpy as np
import cv2
import os,sys,time,g2o
import triangulation


W,H = 1080,720
K = np.array([[0,0,0],[0,0,0],[0,0,0]])
desc_dict = Descriptor()


def calibrate():
    # camera intrinsics
    W, H = 1920//2, 1080//2
    K = np.array([[F,0,W//2],[0,F,H//2],[0,0,1]])
    Kinv = np.linalg.inv(K)
    image = cv2.resize(image, (W,H))
    return image

def generate_SLAM(image):
    image = calibrate(image)
    frame = Camera(desc_dict, image, K)
    if frame.id == 0:
        return
    frame1 = desc_dict.frames[-1]
    frame2 = desc_dict.frames[-2]

    x1,x2,Id = match_#<==========================


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

