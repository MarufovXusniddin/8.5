from .models import Territory, Organization, Building
from .serializers import TerritorySerializer, OrganizationSerializer, BuildingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.


class TerritoryViewSet(ModelViewSet):
    serializer_class = TerritorySerializer
    queryset = Territory.objects.all()
    permission_classes = [IsAdminUser]


class OrganizationViewSet(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated]


class BuildingViewSet(ModelViewSet):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]