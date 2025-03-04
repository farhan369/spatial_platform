from django.contrib.gis.db import models


class SpatialPolygon(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    boundary = models.PolygonField(geography=True, srid=4326)
    category = models.ForeignKey(
        'spatial_api.Category',
        on_delete=models.SET_NULL,
        related_name='polygons',
        null=True,
        blank=True,
    )

    # For choropleth map data
    value = models.FloatField(null=True, blank=True)  # Numeric value for choropleth shading
    value_label = models.CharField(max_length=255, blank=True, null=True)  # Description of the value

    # Additional metadata
    metadata = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

