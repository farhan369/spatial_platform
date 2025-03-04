from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Category(models.Model):
    """
   A category for spatial points.

   Attributes:
       name (str): Unique name of the category.
       description (str): Optional detailed description of the category.
       color (str): Hexadecimal color code for display purposes.
       created_at (datetime): The date and time when the category was created.
       updated_at (datetime): The date and time when the category was last updated.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7, default="#3388ff")  # Hex color code
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SpatialPoint(models.Model):
    """
    Represents a point in 2D space with associated metadata and a geographic location.

    Attributes:
        category (Category): The category this point belongs to.
        name (str): The name of the spatial point.
        description (str): Optional description of the spatial point.
        metadata (dict): Additional metadata stored as JSON.
        location (Point): The geographic location represented as a point (longitude, latitude).
        is_active (bool): Flag to mark if the point is active.
        created_at (datetime): The timestamp when the point was created.
        updated_at (datetime): The timestamp when the point was last updated.
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='points',
        null=True,
        blank=True,
        verbose_name="Category"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True)
    location = models.PointField(geography=True, srid=4326)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.location.x}, {self.location.y})"

    @property
    def longitude(self):
        return self.location.x

    @property
    def latitude(self):
        return self.location.y

    def save(self, *args, **kwargs):
        if not self.location:
            # Default location if none provided
            self.location = Point(0, 0)
        super().save(*args, **kwargs)
