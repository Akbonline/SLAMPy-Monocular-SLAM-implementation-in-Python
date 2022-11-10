"""
Pythonic implementation of an ORB feature matching 
based Monocular-vision SLAM.
"""

import numpy as np
np.seterr(divide='ignore', invalid='ignore')
np.finfo(np.dtype("float32"))
np.finfo(np.dtype("float64"))
import cv2
import os, sys, time
from Camera import denormalize, normalize, triangulate, Camera
from match_frames import generate_match
from descriptor import Descriptor, Point


class SLAM:
    def __init__(self, focal_length = 500, width = 1280, height = 720, psize = 2):
        self.F = focal_length
        # self.W, self.H = width, height
        self.W, self.H = width//2, height//2
        self.K = np.array([[self.F, 0, self.W//2],
                            [0, self.F, self.H//2],
                            [0, 0, 1]])
        self.desc_dict = Descriptor(psize=psize)
        self.desc_dict.create_viewer()
        self.image = None
        print('Init SLAM')

    def calibrate(self, image):
        # camera intrinsics...<================Check this
        return cv2.resize(image, (self.W, self.H))

    def generate(self, image):
        self.image = self.calibrate(image)
        # self.image = image
        frame = Camera(self.desc_dict, self.image, self.K)
        if frame.id == 0:
            return
        frame1 = self.desc_dict.frames[-1]
        frame2 = self.desc_dict.frames[-2]
        x1, x2, Id = generate_match(frame1, frame2)
        frame1.pose = np.dot(Id, frame2.pose)
        for i, idx in enumerate(x2):
            if frame2.pts[idx] is not None:
                frame2.pts[idx].add_observation(frame1, x1[i])
        # homogeneous 3-D coords
        pts4d = triangulate(frame1.pose, frame2.pose, frame1.key_pts[x1], frame2.key_pts[x2])
        # pts4d /= pts4d[:, 3:]
        unmatched_points = np.array([frame1.pts[i] is None for i in x1])
        # print("Adding:  %d points" % np.sum(unmatched_points))
        good_pts4d = (np.abs(pts4d[:, 3]) > 0.005) & (pts4d[:, 2] > 0) & unmatched_points

        for i, p in enumerate(pts4d):
            if not good_pts4d[i]:
                continue
            pt = Point(self.desc_dict, p)
            pt.add_observation(frame1, x1[i])
            pt.add_observation(frame2, x2[i])

        for pt1, pt2 in zip(frame1.key_pts[x1], frame2.key_pts[x2]):
            u1, v1 = denormalize(self.K, pt1)
            u2, v2 = denormalize(self.K, pt2)
            cv2.drawMarker(self.image, (u1, v1), (0, 255, 0), 1, 10, 1, 8)
            # cv2.circle(self.image, (u1, v1), color=(0, 0, 255), radius=2)
            cv2.line(self.image, (u1, v1), (u2, v2), (0, 0, 255), 1)

        # 3-D display
        self.desc_dict.display()

    def __del__(self):
        print('Close SLAM')
        return self.desc_dict.release()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("%s takes in .mp4 as an arg" %sys.argv[0])
        exit(-1)

    cap = cv2.VideoCapture(sys.argv[1]) # Can try Realtime(highly unlikely though)
    # cap.set(cv2.CAP_PROP_POS_FRAMES, 153600)
    # cap.set(cv2.CAP_PROP_POS_FRAMES, 300)
    slam = SLAM(500, 1920, 1080, 2)
    # slam = SLAM()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            slam.generate(frame)
            if slam.image is not None:
                frame_out = cv2.resize(slam.image, (slam.W, slam.H))
                cv2.imshow("SLAM", frame_out)
                # cv2.imshow("SLAM", slam.image)
            # else:
            #     frame1 = cv2.resize(frame, (720,400)) #Resizing the original window
            #     cv2.imshow("SLAM", frame1)
            key = cv2.waitKey(1)
            if key == ord('p'):
                cv2.waitKey(-1)
            elif key == ord('q') or key == 27:
                break
        else:
            break

    cap.release() 
    cv2.destroyAllWindows()

