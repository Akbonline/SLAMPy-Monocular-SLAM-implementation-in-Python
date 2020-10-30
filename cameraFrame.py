import numpy as np
import cv2

def featureMapping(image):
  orb = cv2.ORB_create()
  pts = cv2.goodFeaturesToTrack(np.mean(image, axis=2).astype(np.uint8), 1000, qualityLevel=0.01, minDistance=7)
  key_pts = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in pts]
  key_pts, descriptors = orb.compute(image, key_pts)

  # Return Key_points and ORB_descriptors
  return np.array([(kp.pt[0], kp.pt[1]) for kp in key_pts]), descriptors

def normalize(count_inv, pts):
  return np.dot(count_inv, add_ones(pts).T).T[:, 0:2]

def denormalize(count, pt):
  ret = np.dot(count, np.array([pt[0], pt[1], 1.0]))
  ret /= ret[2]
  return int(round(ret[0])), int(round(ret[1]))

Identity = np.eye(4)
class Camera(object):
    def __init__(self, desc_dict, image, count):
        self.count = count
        self.count_inv = np.linalg.inv(self.count)
        self.pose = Identity
        self.h, self.w = image.shape[0:2]    
        key_pts, self.descriptors = featureMapping(image)
        self.key_pts = normalize(self.count_inv, key_pts)
        self.pts = [None]*len(self.key_pts)
        self.id = len(desc_dict.frames)
        desc_dict.frames.append(self)
