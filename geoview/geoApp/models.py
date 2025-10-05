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
    region = models.CharField(choices=[("Hà Nội", "Hà Nội"), ("Hà Giang", "Hà Giang"), ("Cao Bằng", "Cao Bằng"), ("Bắc Kạn", "Bắc Kạn"), ("Tuyên Quang", "Tuyên Quang"), ("Lào Cai", "Lào Cai"), ("Điện Biên", "Điện Biên"), ("Lai Châu", "Lai Châu"), ("Sơn La", "Sơn La"), ("Yên Bái", "Yên Bái"), ("Hoà Bình", "Hoà Bình"), ("Thái Nguyên", "Thái Nguyên"), ("Lạng Sơn", "Lạng Sơn"), ("Quảng Ninh", "Quảng Ninh"), ("Bắc Giang", "Bắc Giang"), ("Phú Thọ", "Phú Thọ"), ("Vĩnh Phúc", "Vĩnh Phúc"), ("Bắc Ninh", "Bắc Ninh"), ("Hải Dương", "Hải Dương"), ("Hải Phòng", "Hải Phòng"), ("Hưng Yên", "Hưng Yên"), ("Thái Bình", "Thái Bình"), ("Hà Nam", "Hà Nam"), ("Nam Định", "Nam Định"), ("Ninh Bình", "Ninh Bình"), ("Thanh Hóa", "Thanh Hóa"), ("Nghệ An", "Nghệ An"), ("Hà Tĩnh", "Hà Tĩnh"), ("Quảng Bình", "Quảng Bình"), ("Quảng Trị", "Quảng Trị"), ("Thừa Thiên Huế", "Thừa Thiên Huế"), ("Đà Nẵng", "Đà Nẵng"), ("Quảng Nam", "Quảng Nam"), ("Quảng Ngãi", "Quảng Ngãi"), ("Bình Định", "Bình Định"), ("Phú Yên", "Phú Yên"), ("Khánh Hòa", "Khánh Hòa"), ("Ninh Thuận", "Ninh Thuận"), ("Bình Thuận", "Bình Thuận"), ("Kon Tum", "Kon Tum"), ("Gia Lai", "Gia Lai"), ("Đắk Lắk", "Đắk Lắk"), ("Đắk Nông", "Đắk Nông"), ("Lâm Đồng", "Lâm Đồng"), ("Bình Phước", "Bình Phước"), ("Tây Ninh", "Tây Ninh"), ("Bình Dương", "Bình Dương"), ("Đồng Nai", "Đồng Nai"), ("Bà Rịa - Vũng Tàu", "Bà Rịa - Vũng Tàu"), ("Hồ Chí Minh", "Hồ Chí Minh"), ("Long An", "Long An"), ("Tiền Giang", "Tiền Giang"), ("Bến Tre", "Bến Tre"), ("Trà Vinh", "Trà Vinh"), ("Vĩnh Long", "Vĩnh Long"), ("Đồng Tháp", "Đồng Tháp"), ("An Giang", "An Giang"), ("Kiên Giang", "Kiên Giang"), ("Cần Thơ", "Cần Thơ"), ("Hậu Giang", "Hậu Giang"), ("Sóc Trăng", "Sóc Trăng"), ("Bạc Liêu", "Bạc Liêu"), ("Cà Mau", "Cà Mau")], help_text = "figure")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name