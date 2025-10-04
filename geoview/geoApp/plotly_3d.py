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

# Display metadata
print("Raster Metadata:")
print(f"Profile: {profile}")
print(f"Transform: {transform}")
print(f"Bounds: {bounds}")
print(f"CRS: {crs}")

# Get dimensions
height, width = dem_data.shape
print(f"Data dimensions: {height} x {width}")

# Create coordinate arrays for plotting
# Generate x and y coordinates based on the raster bounds and transform
x_coords = np.linspace(bounds.left, bounds.right, width)
y_coords = np.linspace(bounds.bottom, bounds.top, height)
X, Y = np.meshgrid(x_coords, y_coords)

# 1. Create 3D Surface Plot using Plotly (similar to the tutorial)
fig_3d = go.Figure(data=[go.Surface(
    z=dem_data,
    x=X,
    y=Y,
    colorscale='Earth',
    colorbar=dict(title='Elevation (m)'),
    name='DEM Surface'
)])

fig_3d.update_layout(
    title='3D Digital Elevation Model (DEM) - Interactive Terrain Visualization',
    scene=dict(
        xaxis_title='Longitude',
        yaxis_title='Latitude', 
        zaxis_title='Elevation (m)',
        aspectmode='data'
    ),
    width=900,
    height=700
)

# Save 3D plot as HTML
fig_3d.write_html("dem_3d_plotly.html")
print("3D plot saved as 'dem_3d_plotly.html'")

'''
# 2. Create 3D Surface with different colorscale
fig_3d_terrain = go.Figure(data=[go.Surface(
    z=dem_data,
    x=X,
    y=Y,
    colorscale='terrain',
    colorbar=dict(title='Elevation (m)'),
    name='DEM Surface (Terrain)'
)])

fig_3d_terrain.update_layout(
    title='3D DEM with Terrain Colorscale',
    scene=dict(
        xaxis_title='Longitude',
        yaxis_title='Latitude', 
        zaxis_title='Elevation (m)',
        aspectmode='data'
    ),
    width=900,
    height=700
)

# Save terrain 3D plot as HTML
fig_3d_terrain.write_html("dem_3d_terrain_plotly.html")
print("3D terrain plot saved as 'dem_3d_terrain_plotly.html'")
'''