import cv2
import numpy as np

#Recreating bunch of points using Triangulation
#Given the relative poses, calculating the 3d points
def triangulate(pose1, pose2, pts1, pts2):
  
  ret = np.zeros((pts1.shape[0], 4))
  pose1 = np.linalg.inv(pose1)
  pose2 = np.linalg.inv(pose2)
  for i, p in enumerate(zip(pts1, pts2)):
    A = np.zeros((4,4))
    A[0] = p[0][0] * pose1[2] - pose1[0]
    A[1] = p[0][1] * pose1[2] - pose1[1]
    A[2] = p[1][0] * pose2[2] - pose2[0]
    A[3] = p[1][1] * pose2[2] - pose2[1]
    _, _, vt = np.linalg.svd(A)
    ret[i] = vt[3]
  return ret
