import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
def plot_square(TP,ax):
    p1 = TP[0].flatten(); p2 = TP[1].flatten(); p3 = TP[2].flatten(); p4 = TP[3].flatten(); 
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]],zs=[p1[2],p2[2]],c="blue")
    ax.plot([p2[0],p3[0]],[p2[1],p3[1]],zs=[p2[2],p3[2]],c="blue")
    ax.plot([p3[0],p4[0]],[p3[1],p4[1]],zs=[p3[2],p4[2]],c="blue")
    ax.plot([p4[0],p1[0]],[p4[1],p1[1]],zs=[p4[2],p1[2]],c="blue")

def create_image_plane(camera,focalLength,fv):
    hfv = fv/2.0
    P1 = np.array([camera[0]-hfv,camera[1]+hfv,camera[2]+focalLength,1])
    P2 = np.array([camera[0]+hfv,camera[1]+hfv,camera[2]+focalLength,1])
    P3 = np.array([camera[0]+hfv,camera[1]-hfv,camera[2]+focalLength,1])
    P4 = np.array([camera[0]-hfv,camera[1]-hfv,camera[2]+focalLength,1])
    return np.array([P2,P3,P4,P1])

def plane_ray_intersection(plane,p1,p2):
    from sympy import Point3D, Plane, Line, Polygon
    point1 = Point3D(plane[0][0], plane[0][1], plane[0][2])
    point2 = Point3D(plane[1][0], plane[1][1], plane[1][2])
    point3 = Point3D(plane[2][0], plane[2][1], plane[2][2])
    point4 = Point3D(plane[3][0], plane[3][1], plane[3][2])
    
    planeL = Plane(point1,point2, point3)
    planeR = Plane(point2,point3, point4)
    line = Line(Point3D(p1[0],p1[1],p1[2]),Point3D(p2[0],p2[1],p2[2]))
    
    inter1 = planeL.intersection(line)
    inter2 = planeR.intersection(line)

    if len(inter1)>0:
        return inter1[0]
    if len(inter2):
        return inter2[0]

    return None



fig = plt.figure(figsize=(5,5))
ax = plt.axes(projection='3d')

## Camera 1
fv = 3
focalLength = 3
camera1 = (0.5,0.5,0.5,1)
iplane1 = create_image_plane(camera1,focalLength,fv)
ax.scatter(camera1[0],camera1[1],camera1[2])
plot_square(iplane1,ax)

## Camera 2
vx = -5;vy = 0;vz = 0
T = np.array([[1,0,0,vx],[0,1,0,vy],[0,0,1,vz]])
camera2 = np.matmul(camera1,T.T)
ax.scatter(camera2[0],camera2[1],camera2[2])
iplane2 = create_image_plane(camera2,focalLength,fv)
plot_square(iplane2,ax)

P = np.array([-2,0.5,10])
ax.scatter(P[0],P[1],P[2])

ax.plot([P[0],camera1[0]],[P[1],camera1[1]],zs=[P[2],camera1[2]],c="red")
ax.plot([P[0],camera2[0]],[P[1],camera2[1]],zs=[P[2],camera2[2]],c="yellow")


ip1 = plane_ray_intersection(iplane1,camera1,P)
ip2 = plane_ray_intersection(iplane2,camera2,P)
print(ip1)
print(ip2)

ax.scatter(ip1[0], ip1[1], ip1[2])
ax.scatter(ip2[0], ip2[1], ip2[2])


plt.show()