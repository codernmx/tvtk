#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


import numpy as np 
from mayavi import mlab

def test2_1():
	x, y = np.mgrid[-10:10:200j, -10:10:200j]
	z = 100 * np.sin(x * y) / (x * y)

	mlab.figure(bgcolor = (1, 1, 1))
	surf = mlab.surf(z, colormap='cool')

	mlab.show()

def test2_1():
	x, y = np.mgrid[-10:10:200j, -10:10:200j]
	z = 100 * np.sin(x * y) / (x * y)

	mlab.figure(bgcolor = (1, 1, 1))
	surf = mlab.surf(z, colormap='cool')

	lut = surf.module_manager.scalar_lut_manager.lut.table.to_array()

	lut[:, -1] = np.linspace(0, 255, 256)
	surf.module_manager.scalar_lut_manager.lut.table = lut
def test4_1():
	# 场景初始化
	figure = mlab.gcf()

	# 用mlab.points3d建立红色和白色小球的集合
	x1, y1, z1 = np.random.random((3, 10))
	red_glyphs = mlab.points3d(x1, y1, z1, color = (1, 0, 0), resolution = 10)

	x2, y2, z2 = np.random.random((3, 10))
	white_glyphs = mlab.points3d(x2, y2, z2, color = (0.9, 0.9, 0.9), resolution = 10)
	
	outline = mlab.outline(line_width = 3)
	outline.outline_mode = "cornered"
	outline.bounds = (x1[0] - 0.1, x1[0] + 0.1,
					  y1[0] - 0.1, y1[0] + 0.1,
					  z1[0] - 0.1, z1[0] + 0.1,				
		)
	# 处理选取的事件

	glyph_points = red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()


	def picker_callback(picker):
		if picker.actor in red_glyphs.actor.actors:
			point_id = int(picker.point_id / glyph_points.shape[0])
			if point_id != -1:
				x, y, z = x1[point_id], y1[point_id], z1[point_id]
				outline.bounds = (x - 0.1, x + 0.1, 
								  y - 0.1, y + 0.1,
								  z - 0.1, z + 0.1,
									)


	# 建立相应机制

	picker = figure.on_mouse_pick(picker_callback)
	mlab.title("click on the red balls")
	mlab.show()
def test6_1():
	x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
	s = np.sin(x * y *z) / (x * y * z)


	mlab.contour3d(s)
	mlab.show()
def test6_2():
	from mayavi.tools import pipeline
	x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
	s = np.sin(x * y *z) / (x * y * z)

	src = mlab.pipeline.scalar_field(s)
	mlab.pipeline.iso_surface(src, contours = [s.min() + 0.1  * s.ptp(), ], opacity = 0.1)
	mlab.pipeline.iso_surface(src, contours = [s.max() - 0.1  * s.ptp(), ],)
	mlab.pipeline.image_plane_widget(src, plane_orientation = "z_axes", slice_index = 10,)
	mlab.outline()

	mlab.contour3d(s)
	mlab.show()


def test7_1():
	x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
	u =      np.sin(np.pi * x) * np.cos(np.pi * z)
	v = -2 * np.sin(np.pi * y) * np.cos(2 * np.pi * z)
	w = np.cos(np.pi * x) * np.sin(np.pi * z) + np.cos(np.pi * y) * np.sin(2 * np.pi * z)

	obj = mlab.quiver3d(u, v, w)
	mlab.outline()

	mlab.show()

def test7_2():
	x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
	u =      np.sin(np.pi * x) * np.cos(np.pi * z)
	v = -2 * np.sin(np.pi * y) * np.cos(2 * np.pi * z)
	w = np.cos(np.pi * x) * np.sin(np.pi * z) + np.cos(np.pi * y) * np.sin(2 * np.pi * z)

	# obj = mlab.quiver3d(u, v, w)
	# mlab.outline()

	src = mlab.pipeline.vector_field(u, v, w)
	mlab.pipeline.vectors(src, mask_points = 10, scale_factor = 2.0)
	mlab.outline()
	mlab.show()
if __name__=="__main__":
	# test2_1()
	# test6_2()
	test7_2()