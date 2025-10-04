import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits import mplot3d

cwd = os.getcwd()
# Đường dẫn đến file txt chứa dữ liệu thô
#parent_cwd = os.path.join(cwd, os.pardir)
file_path = os.path.join(cwd, "external_data", "temp.dem.tif")


# 1. Open a DEM file
with rasterio.open(file_path) as src:
    # Read the DEM data
    dem_data = src.read(1)  # Read the first band
    height, width = dem_data.shape  
    # Get pixel coordinates for each axis
    y_indices = np.arange(height)
    x_indices = np.arange(width)
    profile = src.profile   # Metadata of the raster

X,Y = np.meshgrid(x_indices, y_indices)
#dem_data = [i * 0.2 for i in dem_data]
dem_data = dem_data * 0.02  # Scale the elevation values

# Display metadata
print("Raster Metadata:")
print(profile)

# https://stackoverflow.com/questions/74995160/improve-smooth-3d-plot-of-demdigital-elevation-model-terrain-surface-from-geot

fig = plt.figure(figsize=(12, 8))
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, dem_data,  cmap='terrain', linewidth=0, antialiased=False)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Elevation (m)')

ax.set_xlabel('X (column)')
ax.set_ylabel('Y (row)')
ax.set_zlabel('Elevation (m)')

ax.set_title('3D DEM evaluation')
plt.show()

'''
# 3. Calculate slope and aspect
# Convert elevation to slope (approximation)
x, y = np.gradient(dem_data)  # Gradient in x and y directions
slope = np.sqrt(x**2 + y**2)  # Approximate slope
aspect = np.arctan2(-y, x)    # Aspect calculation (direction of slope)

# Plot slope
plt.figure(figsize=(10, 6))
plt.imshow(slope, cmap="viridis", interpolation="nearest")
plt.colorbar(label="Slope")
plt.title("Slope Derived from DEM")
plt.show()
'''