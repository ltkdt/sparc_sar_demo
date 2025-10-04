from django.contrib import admin

from .models import DemData, StaticFigure

@admin.register(DemData)
class DemDataAdmin(admin.ModelAdmin):
	list_display = ('name', 'region', 'description')

@admin.register(StaticFigure)
class StaticFigureAdmin(admin.ModelAdmin):
	list_display = ('name', 'region', 'description')