#!/d:\\learn_tvtk\\chapter python3.6.8
# -*- coding: utf-8 -*-


from tvtk.api import tvtk

def ivtk_scene(actors):
	from tvtk.tools import ivtk
	win = ivtk.IVTKWithCrustAndBrowser()
	win.open()
	win.scene.add_actor(actors)
	return win
def event_loop():
	from pyface.api import GUI
	gui = GUI()
	gui.start_event_loop()
def test01():
	s = tvtk.CubeSource(x_length = 1.0, y_length = 2.0, z_length = 3.0)
	m = tvtk.PolyDataMapper(input_connection = s.output_port)
	a = tvtk.Actor(mapper = m)

	win = ivtk_scene(a)
	win.scene.isometric_view()
	event_loop()
def test02():
	import numpy as np 
	x = np.array([0, 3, 9, 15])
	y = np.array([0, 1, 5])
	z = np.array([0, 2, 3])

	r = tvtk.RectilinearGrid()
	r.x_coordinates = x
	r.y_coordinates = y
	r.z_coordinates = z

	r.dimensions = len(x), len(y), len(z)
	

if __name__=="__main__":
	# # test_source()
	# test02()
	# # source1()

	import numpy as np 
	x = np.array([0, 3, 9, 15])
	y = np.array([0, 1, 5])
	z = np.array([0, 2, 3])

	r = tvtk.RectilinearGrid()
	r.x_coordinates = x
	r.y_coordinates = y
	r.z_coordinates = z

	r.dimensions = len(x), len(y), len(z)
