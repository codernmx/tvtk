#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


from tvtk.api import tvtk

def test01():
	s = tvtk.ConeSource(height = 6.0, radius = 2.0)
	m = tvtk.PolyDataMapper(input_connection = s.output_port)

	a = tvtk.Actor(mapper = m)
	r = tvtk.Renderer(background = (1, 0, 0))
	r.add_actor(a)

	w = tvtk.RenderWindow(size= (300, 300))
	w.add_renderer(r)
	i = tvtk.RenderWindowInteractor(render_window = w)

	i.initialize()
	i.start()


if __name__=="__main__":
	test01()