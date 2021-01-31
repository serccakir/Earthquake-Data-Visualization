from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import Countries, Earthquakes


class CountriesSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = Countries
		fields = '__all__'
		geo_field = 'geom'


class EarthquakesSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = Earthquakes
		fields = '__all__'
		geo_field = 'geom'
		
