
# -*- coding: utf-8 -*-
from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI

def test01():
	s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)# 1. 创建数据源，设置参数，并且将参数映射给数据m
	m = tvtk.PolyDataMapper(input_connection=s.output_port)
	a = tvtk.Actor(mapper=m)# 2. 创建背景和行为（可以转动），并且将行为送给 背景
	r = tvtk.Renderer(background=(0, 0, 0))
	r.add_actor(a)
	w = tvtk.RenderWindow(size=(300, 300))# 3. 创建左面窗口的大小，并且将渲染器放入窗口
	w.add_renderer(r)
	i = tvtk.RenderWindowInteractor(render_window=w)# 4. 创建交互界面，将窗口放入
	i.initialize()
	i.start()	

def test_source():
    # 创建一个长方体数据源，并且同时设置其长宽高
    s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
    # 使用PolyDataMapper将数据转换为图形数据
    m = tvtk.PolyDataMapper(input_connection=s.output_port)
    # 创建一个Actor
    a = tvtk.Actor(mapper=m)
    # 创建一个Renderer，将Actor添加进去
    r = tvtk.Renderer(background=(0, 0, 0))
    r.add_actor(a)
    # 创建一个RenderWindow(窗口)，将Renderer添加进去
    w = tvtk.RenderWindow(size=(300,300))
    w.add_renderer(r)
    # 创建一个RenderWindowInteractor（窗口的交互工具)
    i = tvtk.RenderWindowInteractor(render_window=w)
    # 开启交互
    i.initialize()
    i.start()
def test02():
	s = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36)
	m = tvtk.PolyDataMapper(input_connection=s.output_port)
	a = tvtk.Actor(mapper=m)
	r = tvtk.Renderer(background=(0, 0, 0))
	r.add_actor(a)
	w = tvtk.RenderWindow(size=(300, 300))
	w.add_renderer(r)
	i = tvtk.RenderWindowInteractor(render_window=w)
	i.initialize()
	i.start()
def test03():
	s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
	m = tvtk.PolyDataMapper(input_connection=s.output_port)
if __name__=="__main__":
	# test_source()
	test02()