from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry, Point
from rest_framework.decorators import action
from django_filters import rest_framework as filters

from . earthquakes_filter import EarthquakesFilter
from . models import  Countries, Earthquakes
from . serializers import  CountriesSerializer, EarthquakesSerializer


# Create your views here.
class CountriesViewSet(viewsets.ModelViewSet):
	serializer_class = CountriesSerializer
	queryset = Countries.objects.all()
    

class EarthquakesViewSet(viewsets.ModelViewSet):
    serializer_class = EarthquakesSerializer
    queryset = Earthquakes.objects.all()
    filterset_class = EarthquakesFilter
    filter_backends = [filters.DjangoFilterBackend]
   
    @action(detail=False, methods=['get'])
    def get_nearest_earthquakes(self, request):
        x_coords = request.GET.get('x', None)
        y_coords = request.GET.get('y', None)
        if x_coords and y_coords:
            user_location = Point(float(x_coords), float(y_coords), srid=4326)
            nearest_three_earthquakes= Earthquakes.objects.annotate(distance=Distance('geom', user_location)).order_by('distance')[:3]
            serializer = self.get_serializer_class()
            serialized = serializer(nearest_three_earthquakes, many = True)
            print(nearest_three_earthquakes)
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
