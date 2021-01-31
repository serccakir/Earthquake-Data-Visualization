from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters

from django.contrib.gis.measure import D

from .models import Countries, Earthquakes

class EarthquakesFilter(GeoFilterSet):
    country = filters.CharFilter(method = 'get_earthquakes_by_country')

    class Meta:
        model = Earthquakes
        exclude = ['geom']

    def get_earthquakes_by_country(self, queryset, name, value):
        query_ = Countries.objects.filter(name=value)
        if query_:
            obj = query_.first()
            #return queryset.filter(geom__within = obj.geom)
            return queryset.filter(geom__distance_lte = (obj.geom, D(km = 100)))
        return queryset