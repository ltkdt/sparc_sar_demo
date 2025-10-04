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

# 2. Create 2D Heatmap using Plotly
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

# Save 2D plot as HTML
fig_2d.write_html("dem_2d_plotly.html")
print("2D plot saved as 'dem_2d_plotly.html'")

# 3. Calculate slope and aspect (derived from DEM)
x_grad, y_grad = np.gradient(dem_data)
slope = np.sqrt(x_grad**2 + y_grad**2)  # Slope magnitude
aspect = np.arctan2(-y_grad, x_grad)    # Aspect direction

# Create slope visualization
fig_slope = go.Figure(data=go.Heatmap(
    z=slope,
    x=x_coords,
    y=y_coords,
    colorscale='Viridis',
    colorbar=dict(title='Slope (radians)')
))

fig_slope.update_layout(
    title='Slope Derived from DEM',
    xaxis_title='Longitude',
    yaxis_title='Latitude',
    width=900,
    height=600
)

# Save slope plot as HTML
fig_slope.write_html("dem_slope_plotly.html")
print("Slope plot saved as 'dem_slope_plotly.html'")

# 4. Create a combined subplot with DEM and Slope
fig_combined = make_subplots(
    rows=1, cols=2,
    subplot_titles=('Digital Elevation Model', 'Slope Analysis'),
    specs=[[{'type': 'heatmap'}, {'type': 'heatmap'}]]
)

# Add DEM heatmap
fig_combined.add_trace(
    go.Heatmap(
        z=dem_data,
        x=x_coords,
        y=y_coords,
        colorscale='Earth',
        colorbar=dict(title='Elevation (m)'),
        showscale=False
    ),
    row=1, col=1
)

# Add slope heatmap
fig_combined.add_trace(
    go.Heatmap(
        z=slope,
        x=x_coords,
        y=y_coords,
        colorscale='Viridis',
        colorbar=dict(title='Slope (radians)')
    ),
    row=1, col=2
)

fig_combined.update_layout(
    title='DEM Analysis: Elevation and Slope Comparison',
    width=1200,
    height=600
)

# Save combined plot as HTML
fig_combined.write_html("dem_combined_plotly.html")
print("Combined plot saved as 'dem_combined_plotly.html'")

# 5. Create contour plot
fig_contour = go.Figure(data=go.Contour(
    z=dem_data,
    x=x_coords,
    y=y_coords,
    colorscale='Earth',
    contours=dict(
        showlabels=True,
        labelfont=dict(size=12, color="white")
    ),
    colorbar=dict(title='Elevation (m)')
))

fig_contour.update_layout(
    title='DEM Contour Lines',
    xaxis_title='Longitude',
    yaxis_title='Latitude',
    width=900,
    height=600
)

# Save contour plot as HTML
fig_contour.write_html("dem_contour_plotly.html")
print("Contour plot saved as 'dem_contour_plotly.html'")

print("\nAll plots have been generated and saved as HTML files!")
print("You can open them in a web browser for interactive visualization.")