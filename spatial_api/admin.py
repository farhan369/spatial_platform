from django.contrib import admin

from spatial_api import models as spatial_models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class SpatialPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'category', 'is_active')
    search_fields = ('name', 'category__name')


class SpatialPolygonAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'value_label', 'category', 'is_active')
    search_fields = ('name', 'category__name')

admin.site.register(spatial_models.points.Category, CategoryAdmin)
admin.site.register(spatial_models.points.SpatialPoint, SpatialPointAdmin)
admin.site.register(spatial_models.polygon.SpatialPolygon, SpatialPolygonAdmin)