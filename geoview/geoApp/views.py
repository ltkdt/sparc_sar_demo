
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import DateInput, LastActiveForm
from .models import StaticFigure
from django.db.models import Q
from datetime import datetime

import math
import os
import folium
import geopandas as gpd
from folium import GeoJson
from folium.plugins import MousePosition

# Create your views here.
def home(request):
    form = LastActiveForm()
    '''
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
    '''
    shp_dir = os.path.join(os.getcwd(), 'media', 'dbscl')

    m = folium.Map(location=[9.8999, 106.1556], title='Đồng bằng sông Cửu Long' ,zoom_start=9)
    style_dbscl = {'fillColor': "#63a6bc", 'color': "#2f81b5"}
    dbscl = gpd.read_file(os.path.join(shp_dir, 'Songcuulong1.shp'))
    dbscl_geojson = dbscl.to_crs("EPSG:4326").to_json()
    GeoJson(dbscl_geojson, name='dbscl', style_function=lambda x: style_dbscl).add_to(m)
    folium.LayerControl().add_to(m)
    
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

cor_dict = {"Long An": [10.5833, 106.6333], "Hồ Chí Minh": [10.8230, 106.6297], "Đồng Nai": [11.0000, 106.0000], "Bình Dương": [11.1667, 106.6667], "Tây Ninh": [11.3333, 106.1667], "Bến Tre": [10.2333, 106.3833], "An Giang": [10.4667, 105.1667], "Kiên Giang": [10.0333, 105.0667], "Cần Thơ": [10.0333, 105.0667], "Vĩnh Long": [10.2500, 105.9667], "Trà Vinh": [9.9333, 105.9667], "Sóc Trăng": [9.6000, 105.9667], "Bạc Liêu": [9.2833, 105.7500], "Cà Mau": [9.1833, 105.1667]}

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) using Haversine formula
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of earth in kilometers
    r = 6371
    return c * r

def find_nearest_location(input_lat, input_lng, locations_dict):
    """
    Find the nearest location from the dictionary to the input coordinates
    """
    min_distance = float('inf')
    nearest_location = None
    
    for location_name, coords in locations_dict.items():
        lat, lng = coords[0], coords[1]
        distance = calculate_distance(input_lat, input_lng, lat, lng)
        
        if distance < min_distance:
            min_distance = distance
            nearest_location = location_name
    
    return nearest_location, min_distance

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
            
            # Store date range in session for use in output view
            request.session['start_active'] = start_active.isoformat() if start_active else None
            request.session['end_active'] = end_active.isoformat() if end_active else None
        else:
            print("Form is not valid")
            # Clear session data if form is invalid
            request.session['start_active'] = None
            request.session['end_active'] = None
        
        nearest_location, min_distance = find_nearest_location(float(lat), float(lng), cor_dict)
        if min_distance > 100:
            nearest_location = "Không có dữ liệu"
        
        return redirect('output', neartest_location=nearest_location)


def output(request, neartest_location=None):
    # Get the nearest location from URL parameter or set default
    figures = []
    
    if neartest_location and neartest_location != "Không có dữ liệu":
        # Get date range from session
        start_date_str = request.session.get('start_active')
        end_date_str = request.session.get('end_active')
        
        # Parse date strings back to date objects
        start_date = None
        end_date = None
        if start_date_str:
            try:
                start_date = datetime.fromisoformat(start_date_str).date()
            except (ValueError, TypeError):
                start_date = None
        if end_date_str:
            try:
                end_date = datetime.fromisoformat(end_date_str).date()
            except (ValueError, TypeError):
                end_date = None
        
        # Filter figures based on region and date range
        if start_date and end_date:
            # Both dates provided - filter by date range
            figures = StaticFigure.objects.filter(
                region=neartest_location,
                date_taken__range=[start_date, end_date]
            ).order_by('-date_taken')
        elif start_date:
            # Only start date provided - filter from start date onwards
            figures = StaticFigure.objects.filter(
                region=neartest_location,
                date_taken__gte=start_date
            ).order_by('-date_taken')
        elif end_date:
            # Only end date provided - filter up to end date
            figures = StaticFigure.objects.filter(
                region=neartest_location,
                date_taken__lte=end_date
            ).order_by('-date_taken')
        else:
            # No date range - show all figures for the region
            figures = StaticFigure.objects.filter(
                region=neartest_location
            ).order_by('-date_taken')
    
    context = {
        'neartest_location': neartest_location,
        'figures': figures,
        'figure_count': len(figures)
    }
    return render(request, 'geoApp/output.html', context)