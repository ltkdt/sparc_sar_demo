from random import choices
from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class DemData(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    geotiff_file = models.FileField(upload_to='geotiffs/', blank=True, null=True)
    
    #raster = models.RasterField(null=True, blank=True)
    #shapefile = models.FileField(upload_to='shapefiles/', blank=True, null=True)
    
    #border = models.MultiPolygonField(null=True, blank=True)

    def __str__(self):
        return self.name

class StaticFigure(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    figure_file = models.ImageField(upload_to='figures/', blank=True, null=True)
    date_taken = models.DateField(blank=True, null=True)
    region = models.CharField(choices=[("Long An", "Long An"), ("Hồ Chí Minh", "Hồ Chí Minh"), ("Đồng Nai", "Đồng Nai"), ("Bình Dương", "Bình Dương"), ("Tây Ninh", "Tây Ninh"), ("Bến Tre", "Bến Tre"), ("An Giang", "An Giang"), ("Kiên Giang", "Kiên Giang"), ("Cần Thơ", "Cần Thơ"), ("Vĩnh Long", "Vĩnh Long"), ("Trà Vinh", "Trà Vinh"), ("Sóc Trăng", "Sóc Trăng"), ("Bạc Liêu", "Bạc Liêu"), ("Cà Mau", "Cà Mau")], help_text = "figure")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name