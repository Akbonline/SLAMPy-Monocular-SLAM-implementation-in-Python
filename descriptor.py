from multiprocessing import Process, Queue
import numpy as np
import OpenGL.GL as gl
import pangolin
# import g2o

class Point:
    # A Point is a 3-D point in the world
    # Each Point is observed in multiple Frames
    def __init__(self, mapp, loc):
        self.pt = loc
        self.frames = []
        self.idxs = []
        self.id = len(mapp.points)
        mapp.points.append(self)

    def add_observation(self, frame, idx):
        frame.pts[idx] = self
        self.frames.append(frame)
        self.idxs.append(idx)

class Descriptor:
    """Doc Descriptor"""
    def __init__(self, width = 1280, height = 720, psize = 2):
        self.width, self.height = width, height
        self.frames = []
        self.points = []
        self.state = None
        self.q = None
        self.psize = psize
        self.tr = []

    # G2O optimization:
    def optimize(self):
        """ This method does not work, in development """
        err = optimize(self.frames, self.points, local_window, fix_points, verbose, rounds)
        # Key-Point Pruning:
        culled_pt_count = 0
        for p in self.points:
            # <= 4 match point that's old
            old_point = len(p.frames) <= 4 and p.frames[-1].id+7 < self.max_frame
            #handling the reprojection error
            errs = []
            for f,idx in zip(p.frames, p.idxs):
                uv = f.kps[idx]
                proj = np.dot(f.pose[:3], p.homogeneous())
                proj = proj[0:2] / proj[2]
                errs.append(np.linalg.norm(proj-uv))
            if old_point or np.mean(errs) > CULLING_ERR_THRES:
                culled_pt_count += 1
                self.points.remove(p)
                p.delete()

        return err

    def create_viewer(self):
        self.q = Queue()
        self.vp = Process(target=self.viewer_thread, args=(self.q,))
        self.vp.daemon = True
        self.vp.start()

    def release(self):
        # self.vp.kill()
        return self.vp.terminate()

    def viewer_thread(self, q):
        self.viewer_init(self.width, self.height)
        while True:
            self.viewer_refresh(q)

    def viewer_init(self, w, h):
        pangolin.CreateWindowAndBind('Viewport', w, h)
        gl.glEnable(gl.GL_DEPTH_TEST)

        self.scam = pangolin.OpenGlRenderState(
        pangolin.ProjectionMatrix(w, h, 420, 420, w//2, h//2, 0.2, 10000),
                                    pangolin.ModelViewLookAt(0, -10, -8,
                                                            0, 0, 0,
                                                            0, -1, 0))
        self.handler = pangolin.Handler3D(self.scam)

        # Create Interactive View in window
        self.dcam = pangolin.CreateDisplay()
        self.dcam.SetBounds(0.0, 1.0, 0.0, 1.0, -w/h)
        self.dcam.SetHandler(self.handler)

    def viewer_refresh(self, q):
        if self.state is None or not q.empty():
            self.state = q.get()

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glClearColor(0, 0, 0, 0)
        self.dcam.Activate(self.scam)

        # draw keypoints
        # gl.glPointSize(2)
        # gl.glColor3f(0.184314, 0.309804, 0.184314)
        # pangolin.DrawPoints(self.state[1]+1)

        # gl.glPointSize(1)
        # gl.glColor3f(0.3099, 0.3099,0.184314)
        # pangolin.DrawPoints(self.state[1])

        pangolin.glDrawColouredCube()

        gl.glPointSize(self.psize)
        gl.glColor3f(0.2, 0.6, 0.4)
        pangolin.DrawPoints(self.state[1])

        # draw trajectory
        gl.glLineWidth(1)
        gl.glColor3f(1.0, 0.0, 0.0)
        pangolin.DrawLine(self.state[2])

        # draw poses
        gl.glColor3f(0.15, 0.35, 0.75)
        gl.glLineWidth(1)
        gl.glColor3f(0.8, 0.5, 0.2)
        pangolin.DrawCameras(self.state[0], 1.0, 1.0, 1.0)

        pangolin.FinishFrame()

    def display(self):
        if self.q is None:
            return
        poses, pts, cam_pts = [], [], []
        for f in self.frames:
            poses.append(f.pose)
            x = f.pose.ravel()[3]
            y = f.pose.ravel()[7]
            z = f.pose.ravel()[11]
            cam_pts.append([x, y, z])
        for p in self.points:
            pts.append(p.pt)
        self.q.put(( np.array(poses), np.array(pts), np.array(cam_pts) ))

