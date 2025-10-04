from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#from osgeo import gdal
import matplotlib.pyplot as plt
import scipy as sp
import scipy.ndimage
from PIL import Image
from classArrow import *
import matplotlib.cm as cm
import os
import tifffile

cwd = os.getcwd()
# Đường dẫn đến file txt chứa dữ liệu thô
#parent_cwd = os.path.join(cwd, os.pardir)
source_file_dem = os.path.join(cwd, "external_data", "temp.dem.tif")

# Set max number of pixel to: 'None' to prevent errors. Its not nice, but works for that case. Big images will load RAM+CPU heavily (like DecompressionBomb)
Image.MAX_IMAGE_PIXELS = None # first we set no limit to open
img = Image.open(source_file_dem)
y_ratio, x_ratio = img.size


# get aspect ratio of tif file for late plot box-plot-ratio
dem_array = tifffile.imread(source_file_dem)

# create arrays and declare x,y,z variables
lin_x = np.linspace(0, 1, dem_array.shape[0], endpoint=False)
lin_y = np.linspace(0, 1, dem_array.shape[1], endpoint=False)
y, x = np.meshgrid(lin_y, lin_x)
z = dem_array

# Apply gaussian filter
sigma_y = 100
sigma_x = 100
sigma = [sigma_y, sigma_x]
z_smoothed = sp.ndimage.gaussian_filter(z, sigma)

z_smoothed_min = np.amin(z_smoothed)
z_smoothed_max = np.amax(z_smoothed)
z_range = z_smoothed_max - z_smoothed_min

fig = plt.figure(figsize=(12, 10))
ax = plt.axes(projection='3d')
ax.azim = -30
ax.elev = 42
ax.set_box_aspect((x_ratio, y_ratio, ((x_ratio + y_ratio) / 8)))
# If you want to keep the arrow3D, make sure arrows3dplot is available
# ax.arrow3D(1, 1, z_smoothed_max, -1, 0, 1, mutation_scale=20, ec='black', fc='red')
surf = ax.plot_surface(x, y, z_smoothed, cmap='terrain', edgecolor='none')
m = cm.ScalarMappable(cmap=surf.cmap, norm=surf.norm)
m.set_array(z_smoothed)
cbar = fig.colorbar(m, ax=ax, shrink=0.5, aspect=20, ticks=[z_smoothed_min, 0, (z_range * 0.25 + z_smoothed_min), (z_range * 0.5 + z_smoothed_min), (z_range * 0.75 + z_smoothed_min), z_smoothed_max])
cbar.ax.set_yticklabels([f'{z_smoothed_min}', ' ', f'{(z_range * 0.25 + z_smoothed_min)}', f'{(z_range * 0.5 + z_smoothed_min)}', f'{(z_range * 0.75 + z_smoothed_min)}', f'{z_smoothed_max}'])
plt.xticks([])
plt.yticks([])
x_rectangle = [0, 1, 1, 0]
y_rectangle = [0, 0, 1, 1]
z_rectangle = [0, 0, 0, 0]
verts = [list(zip(x_rectangle, y_rectangle, z_rectangle))]
ax.add_collection3d(Poly3DCollection(verts, alpha=0.5))
fig.tight_layout()
plt.show()