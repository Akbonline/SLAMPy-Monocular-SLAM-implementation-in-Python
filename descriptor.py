from multiprocessing import Process, Queue
import numpy as np
import OpenGL.GL as gl
import pangolin
# import g2o

def draw_axis(size):
    gl.glColor3f(1.0, 0.0, 0.0)
    pangolin.DrawLine([[0.0, 0.0, 0.0], [size, 0.0, 0.0]])
    gl.glColor3f(0.0, 1.0, 0.0)
    pangolin.DrawLine([[0.0, 0.0, 0.0], [0.0, -size, 0]])
    gl.glColor3f(0.0, 0.0, 1.0)
    pangolin.DrawLine([[0.0, 0.0, 0.0], [0.0, 0.0, size]])

def draw_grid(col):
    gl.glColor3f(0.7, 0.7, 0.7)
    for line in np.arange(col+1):
        pangolin.DrawLine([[line, 0.0, 0.0], [line, 0.0, col]])
        pangolin.DrawLine([[0.0, 0.0, line], [col, 0.0, line]])

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
        self.q3D = None # 3D data queue
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
        self.q3D = Queue()
        self.vp = Process(target=self.viewer_thread, args=(self.q3D,))
        self.vp.daemon = True
        self.vp.start()

    def release(self):
        # self.vp.kill()
        return self.vp.terminate()

    def viewer_thread(self, q3d):
        self.viewer_init(self.width, self.height)
        while True:
            self.viewer_refresh(q3d)

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

    def viewer_refresh(self, q3d):
        if self.state is None or not q3d.empty():
            self.state = q3d.get()

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glClearColor(0, 0, 0, 0)
        self.dcam.Activate(self.scam)

        # pangolin.glDrawColouredCube()
        # draw Axis and Grid
        draw_axis(3.0)
        draw_grid(5.0)

        # draw keypoints
        gl.glPointSize(self.psize)
        gl.glColor3f(0.2, 0.6, 0.4)
        pangolin.DrawPoints(self.state[1])

        # draw trajectory
        gl.glLineWidth(1)
        gl.glColor3f(1.0, 0.0, 0.0)
        pangolin.DrawLine(self.state[2])

        # draw all poses
        gl.glColor3f(0.75, 0.75, 0.15)
        pangolin.DrawCameras(self.state[0], 0.75, 0.75, 0.75)

        # draw current pose
        gl.glColor3f(1.0, 0.0, 0.0)
        pangolin.DrawCameras(self.state[3], 1.5, 0.75, 1.0)

        pangolin.FinishFrame()

    def put3D(self):
        ''' put 3D data in Queue '''
        if self.q3D is None:
            return
        poses, pts, cam_pts = [], [], []
        # get last element of list
        current_pose = [self.frames[-1].pose]
        for f in self.frames:
            x = f.pose.ravel()[3]
            y = f.pose.ravel()[7]
            z = f.pose.ravel()[11]
            cam_pts.append([x, y, z])
            poses.append(f.pose)
        for p in self.points:
            pts.append(p.pt)
        self.q3D.put((np.array(poses[:-1]), np.array(pts),
                    np.array(cam_pts), np.array(current_pose) ))

