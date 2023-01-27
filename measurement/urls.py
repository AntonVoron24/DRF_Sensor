from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('sensor', SensorViewSet)
router.register('measurement', MeasurementViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
