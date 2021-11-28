#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


from tvtk.api import tvtk
from chapter2_2 import ivtk_scene, event_loop


plot3d = tvtk.MultiBlockPLOT3DReader(
	xyz_file_name = "combxyz.bin",
	q_file_name = "combq.bin",
	scalar_function_number = 100,
	vector_function_number = 200
	)
plot3d.update() # 让plot3d 计算并且读取数据

grid = plot3d.output.get_block(0) #获取读入的数据集对象

# 对数据进行随机选择，每50个点选择一个点
mask = tvtk.MaskPoints(random_mode = True, on_ratio = 50)
mask.set_input_data(grid)

glyph_source = tvtk.ArrowSource()

# 绘制箭头
glyph = tvtk.Glyph3D(input_connection = mask.output_port, scale_factor = 4)
glyph.set_source_connection(glyph_source.output_port)

m = tvtk.PolyDataMapper(scalar_range= grid.point_data.scalars.range,
						input_connection = glyph.output_port)
a = tvtk.Actor(mapper = m)

win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()
