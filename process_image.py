# http://emmanuelle.github.io/segmentation-of-3-d-tomography-images-with-python-and-scikit-image.html

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
from time import time

from scipy import stats
vmin, vmax = stats.scoreatpercentile(dat, (0.5, 99.5))

# dat = np.fromfile('img/petry_plate_1.jpg', dtype=np.float32)
#
# dat.shape

dat = np.clip(dat, vmin, vmax)
dat = (dat - vmin) / (vmax - vmin)
plt.imshow(dat[10], cmap='gray')

img = mping.imread('img/petry_plate_1.jpg')
imgplot = plt.imshow(img, cmap='gray', vmin=10, vmax=100)
plt.colorbar()
plt.show(imgplot)
