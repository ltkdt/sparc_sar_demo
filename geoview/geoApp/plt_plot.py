import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()
# Đường dẫn đến file txt chứa dữ liệu thô
#parent_cwd = os.path.join(cwd, os.pardir)
file_path = os.path.join(cwd, "external_data", "temp.dem.tif")

# 1. Open a DEM file
#file_path = "path_to_your_dem.tif"  # Replace with the path to your DEM file
with rasterio.open(file_path) as src:
    # Read the DEM data
    dem_data = src.read(1)  # Read the first band
    profile = src.profile   # Metadata of the raster

# Display metadata
print("Raster Metadata:")
print(profile)

# 2. Visualize the DEM
plt.figure(figsize=(10, 6))
im = plt.imshow(dem_data, cmap="terrain")
plt.title("Digital Elevation Model (DEM)")
plt.colorbar(im, label="Elevation (m)")
plt.show()

# 3. Calculate slope and aspect
# Convert elevation to slope (approximation)
x, y = np.gradient(dem_data)  # Gradient in x and y directions
slope = np.sqrt(x**2 + y**2)  # Approximate slope
aspect = np.arctan2(-y, x)    # Aspect calculation (direction of slope)

# Plot slope
plt.figure(figsize=(10, 6))
im_slope = plt.imshow(slope, cmap="viridis", interpolation="nearest")
plt.colorbar(im_slope, label="Slope")
plt.title("Slope Derived from DEM")
plt.show()