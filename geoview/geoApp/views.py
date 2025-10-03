from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import DateInput, LastActiveForm


import os
import folium
import geopandas as gpd
from folium import GeoJson
from folium.plugins import MousePosition

# Create your views here.
def home(request):
    form = LastActiveForm()
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')

    m = folium.Map(location=[0.0236, 37.9062], zoom_start=6)

    style_Kenya_county_dd = {'fillColor': '#228B22', 'color': '#228B22'}
    style_kenya_wetlands = {'color': 'blue'}
    style_kenya_all_towns = {'color': 'red'}
    style_kenya_highland_roads = {'color': 'yellow'}
    style_kenya_forestranges = {'color': 'green'}

    Kenya_county_dd = gpd.read_file(os.path.join(shp_dir, 'Kenya_county_dd.shp'))
    Kenya_county_dd_geojson = Kenya_county_dd.to_crs("EPSG:4326").to_json()

    # to_crs("EPSG:4326")

    kenya_wetlands = gpd.read_file(os.path.join(shp_dir, 'kenya_wetlands.shp'))
    kenya_wetlands_geojson = kenya_wetlands.to_crs("EPSG:4326").to_json()

    kenya_all_towns = gpd.read_file(os.path.join(shp_dir, 'kenya_all_towns.shp'))
    kenya_all_towns_geojson = kenya_all_towns.to_crs("EPSG:4326").to_json()

    kenya_highland_roads = gpd.read_file(os.path.join(shp_dir, 'kenya_highland_roads.shp'))
    kenya_highland_roads_geojson = kenya_highland_roads.to_crs("EPSG:4326").to_json()

    #kenya_forestranges = gpd.read_file(os.path.join(shp_dir, 'kenya_forestranges.shp'))
    #kenya_forestranges_geojson = kenya_forestranges.to_crs("EPSG:4326").to_json()

    GeoJson(Kenya_county_dd_geojson, name='Kenya_counties', style_function=lambda x: style_Kenya_county_dd).add_to(m)
    GeoJson(kenya_wetlands_geojson, name='kenya_wetlands', style_function=lambda x: style_kenya_wetlands).add_to(m)

    # Create a feature group for kenya_all_towns layer
    kenya_all_towns_fg = folium.FeatureGroup(name='kenya_all_towns')
    # Iterate over the points and add colored circles to the feature group
    for _, row in kenya_all_towns.iterrows():
        folium.CircleMarker(location=[row['geometry'].y, row['geometry'].x], radius=2, fill=True, color='red', fill_opacity=1).add_to(kenya_all_towns_fg)
    kenya_all_towns_fg.add_to(m)

    GeoJson(kenya_highland_roads_geojson, name='kenya_highland_roads', style_function=lambda x: style_kenya_highland_roads).add_to(m)
    #GeoJson(kenya_forestranges_geojson, name='kenya_forestranges', style_function=lambda x: style_kenya_forestranges).add_to(m)

    folium.LayerControl().add_to(m)
    # m.get_root().html.add_child(JavascriptLink('./templates/geoApp/folium_click.js'))

    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"

    MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(m)

    popup1 = folium.LatLngPopup()
    m.add_child(popup1)

    m = m._repr_html_()
    context = {'my_map': m, 'form': form}
    return render(request, 'geoApp/home.html', context)

@csrf_exempt
def rev_click(request):
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        print(f"Received coordinates: Latitude={lat}, Longitude={lng}")
        # You can process the coordinates as needed here
        # For example, save them to the database or perform some calculations
        form = LastActiveForm(request.POST)
        if form.is_valid():
            start_active = form.cleaned_data['start_active']
            end_active = form.cleaned_data['end_active']
            print(f"Start Active: {start_active}, End Active: {end_active}")
            # Process the form data as needed
        else:
            print("Form is not valid")

    return redirect('home')
