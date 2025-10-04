import rasterio
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os

cwd = os.getcwd()
# Đường dẫn đến file txt chứa dữ liệu thô
file_path = os.path.join(cwd, "external_data", "temp.dem.tif")

# Read DEM data using rasterio
with rasterio.open(file_path) as src:
    # Read the DEM data
    dem_data = src.read(1)  # Read the first band
    profile = src.profile   # Metadata of the raster
    transform = src.transform  # Geospatial transform
    bounds = src.bounds  # Bounding box
    crs = src.crs  # Coordinate reference system

'''
# Display metadata
print("Raster Metadata:")
print(f"Profile: {profile}")
print(f"Transform: {transform}")
print(f"Bounds: {bounds}")
print(f"CRS: {crs}")
'''

# Get dimensions
height, width = dem_data.shape
print(f"Data dimensions: {height} x {width}")

# Create coordinate arrays for plotting
# Generate x and y coordinates based on the raster bounds and transform
x_coords = np.linspace(bounds.left, bounds.right, width)
y_coords = np.linspace(bounds.bottom, bounds.top, height)
X, Y = np.meshgrid(x_coords, y_coords)

# 1. Create 2D Heatmap using Plotly
fig_2d = go.Figure(data=go.Heatmap(
    z=dem_data,
    x=x_coords,
    y=y_coords,
    colorscale='Earth',
    colorbar=dict(title='Elevation (m)')
))

fig_2d.update_layout(
    title='2D Digital Elevation Model (DEM) - Heatmap View',
    xaxis_title='Longitude',
    yaxis_title='Latitude',
    width=900,
    height=600
)
fig_2d.write_html("dem_3d_plotly.html")
print("2D plot saved as 'dem_3d_plotly.html'")