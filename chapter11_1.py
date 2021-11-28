#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


from numpy import sqrt, sin, mgrid
from traits.api import HasTraits, Instance
from traitsui.api import View, Item
from tvtk.pyface.scene_editor import SceneEditor 
from mayavi.tools.mlab_scene_model import MlabSceneModel
from mayavi.core.ui.mayavi_scene import MayaviScene


class ActorView(HasTraits):
	scene = Instance(MlabSceneModel, ())

	View = View(
		Item(name = "scene",
			editor = SceneEditor(scene_class = MayaviScene),
			show_label = False,
			resizable = True,
			height = 500,
			width = 500
			),
		resizable = True
		)


	"""docstring for ActorView"""
	def __init__(self, **traits):
		# super(ActorView, self).__init__()
		HasTraits.__init__(self, **traits)
		self.generate_data()
	def generate_data(self):
		x, y = mgrid[-2:2:100j, -2:2:100j]
		r = 10 * sqrt(x ** 2 + y ** 2)
		z = sin(r) / r

		self.scene.mlab.surf(x, y, z, colormap = "cool")
def test01():
	a = ActorView()
	a.configure_traits()


if __name__=="__main__":
	test01()