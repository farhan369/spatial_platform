from rest_framework.routers import DefaultRouter

from spatial_api import views

router = DefaultRouter()
router.register(r'points', views.PointViewSet)
router.register(r'polygons', views.PolygonViewSet)

urlpatterns = router.urls
