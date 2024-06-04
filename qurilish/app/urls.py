from django.urls import path, include
from .views import TerritoryViewSet, OrganizationViewSet, BuildingViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('territory', TerritoryViewSet)
router.register('organization', OrganizationViewSet)
router.register('building', BuildingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
]