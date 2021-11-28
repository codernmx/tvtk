#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-

from tvtk.api import tvtk
from chapter2_2 import ivtk_scene, event_loop

# def readData():
# 	plot3d = tvtk.MultiBlockPLOT3DReader(
# 		xyz_file_name = "combxyz.bin",
# 		q_file_name = "combq.bin",
# 		scalar_function_number = 100,
# 		vector_function_number = 200
# 		)
# 	plot3d.update() # 让plot3d 计算并且读取数据
# 	return plot3d
# def test02():
# 	plot3d = readData()
# 	grid = plot3d.output.get_block(0) #获取读入的数据集对象




# plot3d = readData()
# grid = plot3d.output.get_block(0)
# con = tvtk.ContourFilter() # 创建等值面对象
# con.set_input_data(grid)	# 等值面对象和数据及相连
# con.generate_values(10, grid.point_data.scalars.range) # 指定轮廓数和数据范围
# # 设定映射器的变量范围和属性
# m = tvtk.PolyDataMapper(scalar_range = grid.point_data.scalars.range, input_connection = con.output_port)
# a = tvtk.Actor(mapper = m)
# a.property.opacity = 0.5
# # 窗体绘制
# win = ivtk_scene(a)
# event_loop()


	 
plot3d = tvtk.MultiBlockPLOT3DReader(
		xyz_file_name="combxyz.bin",
		q_file_name="combq.bin",
		scalar_function_number=100, vector_function_number=200
	)#读入Plot3D数据
plot3d.update()#让plot3D计算其输出数据
grid = plot3d.output.get_block(0)#获取读入的数据集对象
 
con = tvtk.ContourFilter()#创建等值面对象  
con.set_input_data(grid)
con.generate_values(10, grid.point_data.scalars.range)#指定轮廓数和数据范围
 
#设定映射器的变量范围属性
m = tvtk.PolyDataMapper(scalar_range = grid.point_data.scalars.range,
						input_connection=con.output_port)
a = tvtk.Actor(mapper = m)
a.property.opacity = 0.5#设定透明度为0.5
#窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()
