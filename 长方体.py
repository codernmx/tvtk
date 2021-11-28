#!/d:\\learn_tvtk\\chapter python3.7
# -*- coding: utf-8 -*-

from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI


def test01():
	s = tvtk.CubeSource(x_length = 1.0, y_length = 2.0, z_length = 3.0)
	m = tvtk.PolyDataMapper(input_connection = s.output_port)
	a = tvtk.Actor(mapper = m)

	# 1. 创建一个带有Crust的窗口
	gui = GUI()
	win = tvtk.TVTKWithCrustAndBrower()
	win.open()
	win.scene.add_actor(a)

	gui.start_event_loop()

# 添加 from tvtk.tools import ivtk 时候，
# 若报错 No module named Pygments
# 则 pip install Pygments

# from tvtk.api import tvtk
# from tvtk.tools import ivtk
# from pyface.api import GUI
def source1():
	s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
	m = tvtk.PolyDataMapper(input_connection=s.output_port)
	a = tvtk.Actor(mapper=m)
	 
	#创建一个带Crust（Python Shell）的窗口
	gui = GUI()
	win = ivtk.IVTKWithCrustAndBrowser()
	win.open()
	win.scene.add_actor(a)
	 
	#开始界面消息循环
	gui.start_event_loop()

if __name__=="__main__":
	# test_source()
	# test01()
	source1()