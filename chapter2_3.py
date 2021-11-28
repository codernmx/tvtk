#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


from tvtk.api import tvtk
from chapter2_2 import ivtk_scene, event_loop

def test01():
	s = tvtk.STLReader(file_name="python.stl")
	m = tvtk.PolyDataMapper(input_connection=s.output_port)
	a = tvtk.Actor(mapper = m)

	win = ivtk_scene(a)
	win.scene.isometric_view()
	event_loop()

def readData():
	plot3d = tvtk.MultiBlockPLOT3DReader(
		xyz_file_name = "combxyz.bin",
		q_file_name = "combq.bin",
		scalar_function_number = 100,
		vector_function_number = 200
		)
	plot3d.update()
	return plot3d
def test02():
	plot3d = readData()
	grid = plot3d.output.get_block(0)
if __name__=="__main__":
	plot3d = readData()
	grid = plot3d.output.get_block(0)
