from django.contrib import admin
from .models import Territory, Organization, Building

# Register your models here.


class TerritoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'formed', 'territory')
    list_display_links = ('name',)


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'field', 'floor', 'parking', 'playground', 'elevator', 'organization', 'territory')
    list_display_links = ('name',)


admin.site.register(Territory, TerritoryAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Building, BuildingAdmin)