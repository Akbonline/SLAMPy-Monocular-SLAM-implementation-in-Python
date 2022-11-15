import numpy as np
import cv2
# from numba import njit

def featureMappingORB(frame):
    orb = cv2.ORB_create()
    # pts = cv2.goodFeaturesToTrack(np.mean(frame, axis=2).astype(np.uint8), 1000, qualityLevel=0.01, minDistance=7)
    pts = cv2.goodFeaturesToTrack(np.mean(frame, axis=2).astype(np.uint8), 1000, qualityLevel=0.01, minDistance=7)
    key_pts = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in pts]
    key_pts, descriptors = orb.compute(frame, key_pts)
    # Return Key_points and ORB_descriptors
    return np.array([(kp.pt[0], kp.pt[1]) for kp in key_pts]), descriptors

def featureMappingAKAZE(frame):
    detect = cv2.AKAZE_create()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    key_pts, des = detect.detectAndCompute(frame_gray, None)
    return np.array([(kp.pt[0], kp.pt[1]) for kp in key_pts]), des

def featureMappingSURF(frame):
    detect = cv2.xfeatures2d.SURF_create(2000)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    key_pts, des = detect.detectAndCompute(frame_gray, None)
    return np.array([(kp.pt[0], kp.pt[1]) for kp in key_pts]), des

def normalize(count_inv, pts):
    return np.dot(count_inv, np.concatenate([pts, np.ones((pts.shape[0], 1))], axis=1).T).T[:, 0:2]

def denormalize(count, pt):
    ret = np.dot(count, np.array([pt[0], pt[1], 1.0]))
    ret /= ret[2]
    return int(round(ret[0])), int(round(ret[1]))

# @njit
def triangulate(pose1, pose2, pts1, pts2):
    """
    change on cv.triangulatePoints
    
    Recreating bunch of points using Triangulation
    Given the relative poses, calculating the 3d points
    """
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
    return ret / ret[:, 3:]

Identity = np.eye(4)
FT = {'ORB':featureMappingORB, 'AKAZE':featureMappingAKAZE}
class Camera:
    def __init__(self, desc_dict, image, count, algorithm):
        # self.count = count
        self.count_inv = np.linalg.inv(count)
        self.pose = Identity
        self.h, self.w = image.shape[0:2]
        key_pts, self.descriptors = FT[algorithm](image)
        self.key_pts = normalize(self.count_inv, key_pts)
        self.pts = [None]*len(self.key_pts)
        self.id = len(desc_dict.frames)
        desc_dict.frames.append(self)

