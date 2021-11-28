#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


import numpy as np 
from mayavi import mlab

def test01():
	t = np.linspace(0, 4 * np.pi, 20)
	x = np.sin(2 * t)
	y = np.cos(t)
	z = np.cos(2 * t)

	s = 2 + np.sin(t)

	points = mlab.points3d(x, y, z, s, colormap="Blues", scale_factor=0.25)
	mlab.show()


def test02():
	n_mer, n_long= 6, 11
	dphi = np.pi / 1000
	phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
	mu = phi * n_mer
	x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
	y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
	z = np.sin(n_long * mu / n_mer) * 0.5

	l = mlab.plot3d(x, y, z, np.sin(mu), tube_radius = 0.025, colormap = "Spectral")
	mlab.show()


def test03():
	s = np.random.random((10, 10))

	img = mlab.imshow(s, colormap = "gist_earth")
	mlab.show()
def f(x, y):
	return np.sin(x - y) + np.cos(x + y)
	
def test04():
	x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
	s = mlab.surf(x, y, f)
	mlab.show()

def test05():
	x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
	s = mlab.contour_surf(x, y, f)
	mlab.show()
def test06():
	x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
	scalars = x * x + y * y + z * z
	obj = mlab.contour3d(scalars, contours = 8, transparent = True)
	mlab.show()

def test07():
	x, y, z = np.mgrid[-2:3, -2:3, -2:3]
	r = np.sqrt(x**2 + y ** 2 + z ** 4)
	u = y * np.sin(r) / (r + 0.001)
	v = -x * np.sin(r) / (r + 0.001)
	w = np.zeros_like(z)

	obj = mlab.quiver3d(x, y, z, u, v, w, line_width = 3, scale_factor = 1)
	mlab.show()
	pass
	
if __name__=="__main__":
	test07()