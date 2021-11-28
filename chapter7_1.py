#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


import os
from os.path import join
import tarfile
from mayavi import mlab
import numpy as np


def test01():
	dragon_tar_file = tarfile.open("dragon.tar.gz")
	try:
		os.mkdir("dragon_data")
	except:
		pass
	dragon_tar_file.extractall("dragon_data")
	dragon_tar_file.close()
	dragon_ply_file = join("dragon_data", "dragon_recon", "dragon_vrip.ply")


	mlab.pipeline.surface(mlab.pipeline.open(dragon_ply_file))
	mlab.show()

	import shutil
	shutil.rmtree("dragon_data")

def test02():
	import zipfile
	hgt = zipfile.ZipFile("N36W113.hgt.zip").read("N36W113.hgt")
	data = np.fromstring(hgt, '>i2')
	data.shape = (3601, 3601)
	data = data.astype(np.float32)
	data = data[:1000, 900:1000]
	data[data == -32768] = data[data > 0].min()

	mlab.figure(size = (400, 320), bgcolor = (0.16, 0.28, 0.46))
	mlab.surf(data, colormap = "gist_earth", warp_scale = 0.2, vmin = 1200, vmax = 1610)

	del data
	mlab.view(-5.9, 83, 570, [5.3, 20, 238])
	mlab.show()

if __name__=="__main__":
	test02()