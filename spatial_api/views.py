from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from spatial_api.models import points as point_models
from spatial_api.models import polygon as polygon_models
from spatial_api import serializers as spatial_serial
from spatial_api import filters as spatial_filters


class PointViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch',]
    queryset = point_models.SpatialPoint.objects.all()
    serializer_class = spatial_serial.PointSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = spatial_filters.SpatialPointFilter


class PolygonViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch',]
    queryset = polygon_models.SpatialPolygon.objects.all()
    serializer_class = spatial_serial.PolygonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = spatial_filters.SpatialPolygontFilter