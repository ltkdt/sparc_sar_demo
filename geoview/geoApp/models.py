from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class GeoSpatialData(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    description = models.TextField(blank=True)
    geotiff_file = models.FileField(upload_to='geotiffs/', blank=True, null=True)
    raster = models.RasterField(null=True, blank=True)
    shapefile = models.FileField(upload_to='shapefiles/', blank=True, null=True)
    border = models.MultiPolygonField(null=True, blank=True)

    def __str__(self):
        return self.name
