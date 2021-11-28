#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-

from tvtk.api import tvtk
from chapter2_2 import ivtk_scene, event_loop
from tvtk.common import configure_input

plot3d = tvtk.MultiBlockPLOT3DReader(
	xyz_file_name = "combxyz.bin",
	q_file_name = "combq.bin",
	scalar_function_number = 100,
	vector_function_number = 200
	)
plot3d.update() # 让plot3d 计算并且读取数据

grid = plot3d.output.get_block(0) #获取读入的数据集对象

outline = tvtk.StructuredGridOutlineFilter()
configure_input(outline, grid)

m = tvtk.PolyDataMapper(input_connection = outline.output_port)
a = tvtk.Actor(mapper = m)

a.property.color = 0.3, 0.3, 0.3

win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()