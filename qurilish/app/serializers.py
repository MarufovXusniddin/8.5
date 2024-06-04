from rest_framework.serializers import ModelSerializer
from .models import Territory, Organization, Building


class TerritorySerializer(ModelSerializer):
    class Meta:
        model = Territory
        fields = '__all__'


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'
