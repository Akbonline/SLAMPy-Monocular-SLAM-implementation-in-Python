import numpy as np
import cv2

Identity = np.eye(4)
class Camera(object):
  def __init__(self, mapp, img, K):
    self.K = K
    self.Kinv = np.linalg.inv(self.K)
    self.pose = Identity
    self.h, self.w = img.shape[0:2]

    kps, self.des = extract(img)
    self.kps = normalize(self.Kinv, kps)
    self.pts = [None]*len(self.kps)

    self.id = len(mapp.frames)
    mapp.frames.append(self)
