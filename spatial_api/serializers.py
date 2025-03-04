from rest_framework import serializers

from spatial_api.models import points as point_models
from spatial_api.models import polygon as polygon_models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = point_models.Category
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=point_models.Category.objects.all(),
        required=False,
        write_only=True
    )
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = point_models.SpatialPoint
        fields = '__all__'


class PolygonSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=point_models.Category.objects.all(),
        required=False,
        write_only=True
    )
    category_detail = CategorySerializer(source='category', read_only=True)
    class Meta:
        model = polygon_models.SpatialPolygon
        fields = '__all__'