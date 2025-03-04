from django.contrib.gis.db import models


class SpatialPolygon(models.Model):
    """
      Represents a polygon with a geographic boundary and optional choropleth data.

      Attributes:
          category (Category): The category this polygon belongs to.
          name (str): The name of the spatial polygon.
          description (str): Optional description of the polygon.
          boundary (Polygon): The geographic boundary defined as a polygon.
          value (float): Numeric value used for choropleth map shading.
          value_label (str): Label or description associated with the numeric value.
          metadata (dict): Additional metadata stored as JSON.
          is_active (bool): Flag to mark if the polygon is active.
          created_at (datetime): The timestamp when the polygon was created.
          updated_at (datetime): The timestamp when the polygon was last updated.
      """
    category = models.ForeignKey(
        'spatial_api.Category',
        on_delete=models.SET_NULL,
        related_name='polygons',
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    boundary = models.PolygonField(geography=True, srid=4326)

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

