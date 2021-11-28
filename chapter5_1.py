#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


# x = [[-1, 1, 1, -1, -1], [-1, 1, 1, -1, -1]]
# y = [[-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
# z = [[1, 1, -1, -1, 1], [1, 1, -1, -1, 1]]

from numpy import pi, sin, cos, mgrid
from mayavi import mlab

def test01():
	dphi, dtheta = pi/250.0, pi/250.0
	[phi, theta] = mgrid[0:pi+dphi * 1.5:dphi, 0:2*pi+dtheta*1.5:dtheta]
	m0, m1, m2, m3, m4, m5, m6, m7 = 4, 3, 2, 3, 6, 2, 6, 4
	r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
	x = r * sin(phi) * cos(theta)
	y = r * cos(phi)
	z = r * sin(phi) * sin(theta)
	s = mlab.mesh(x, y, z, representation = "wireframe", line_width = 1.0)
	mlab.show()

if __name__=="__main__":
	dphi, dtheta = pi/250.0, pi/250.0
	[phi, theta] = mgrid[0:pi+dphi * 1.5:dphi, 0:2*pi+dtheta*1.5:dtheta]
	m0, m1, m2, m3, m4, m5, m6, m7 = 4, 3, 2, 3, 6, 2, 6, 4
	r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
	x = r * sin(phi) * cos(theta)
	y = r * cos(phi)
	z = r * sin(phi) * sin(theta) 
	s = mlab.mesh(x, y, z, representation = "wireframe", line_width = 1.0)
	mlab.show()
