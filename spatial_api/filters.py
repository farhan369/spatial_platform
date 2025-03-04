import django_filters

from spatial_api.models import points as point_model
from spatial_api.models import polygon as polygon_model

class SpatialPointFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(
        field_name='category__id',
        lookup_expr='exact'
    )

    class Meta:
        model = point_model.SpatialPoint
        fields = ['category']


class SpatialPolygontFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(
        field_name='category__id',
        lookup_expr='exact'
    )

    class Meta:
        model = polygon_model.SpatialPolygon
        fields = ['category']