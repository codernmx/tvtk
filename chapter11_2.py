#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


from numpy import pi, sqrt, sin, mgrid, arange
from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Item
from tvtk.pyface.scene_editor import SceneEditor 
from mayavi.tools.mlab_scene_model import MlabSceneModel
from mayavi.core.ui.mayavi_scene import MayaviScene
from mayavi.core.api import PipelineBase


dphi = pi / 300
phi = arange(0.0, 2 * pi + 0.5 * dphi, dphi, 'd')

def curve(n_mer, n_long):
	mu = phi*n_mer
	x = cos(mu) * (1 + cos(n_long * mu / n_mer) * 0.5)
	y = sin(mu) * (1 + cos(n_long * mu / n_mer) * 0.5)
	z = 0.5 * sin(n_long * mu / n_mer)
	t = sin(mu)
	return x, y, z, t

class myModel(HasTraits):
	n_meridional = range(0, 30, 6)
	n_longitudinal = range(0, 30, 11)

	scene = Instance(MlabSceneModel, ())

	plot = Instance(PipelineBase)

	@on_trait_change("n_meridional, n_longitudinal, scene.activated")
	def update_plot(self):
		x, y, z, t = curve(n_meridional, n_longitudinal)
		if self.plot is None:
			self.plot = self.scene.mlab.plot3d(x, y, z, t, tube_radius = 0.025, colormap = "Spectral")
		else:
			self.plot.mlab_source.set(x, y, z, scalars = t)
def test01():
	model = myModel()
	model.configure_traits()

if __name__=="__main__":
	test01()


