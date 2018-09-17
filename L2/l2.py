"""

"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
def green(im):
	return im[:,:,1]
def red(im):
	return im[:,:,0]
def blue(im):
	return im[:,:,2]
def plot_row(grayim,index):
	y = grayim[index,:]
	x = np.arange(len(y))
	plt.plot(x,y)
	plt.show()

def plot_3d(img):
	w,h = img.shape
	fig = plt.figure(figsize=(8, 3))
	ax1 = fig.add_subplot(111, projection='3d')
	_x = np.arange(w)
	_y = np.arange(h)
	_xx, _yy = np.meshgrid(_x, _y)
	x, y = _xx.ravel(), _yy.ravel()
	z = img.flatten()
	bottom = np.zeros_like(z)
	print "plotting"
	ax1.bar3d(x, y, bottom,1,1,z, shade=True)
	print "showing"
	plt.show()

def imshow(im):
	cv.imshow('image',im)
	cv.waitKey(0)


messi = cv.imread("messi.jpg")
### Messi Ball
ball = messi[280:340, 330:390]
messi[273:333, 100:160] = ball

### Messi Green
messigreen = green(messi)
#plot_row(messigreen,10)
plot_3d(messigreen)


