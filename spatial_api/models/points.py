from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Category(models.Model):
    """
    A category for spatial points.
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
    A point in the 2D space with additional fields for name, description, and location.
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
