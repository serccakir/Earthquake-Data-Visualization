from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from backend.models import Countries, Earthquakes

# Create your views here.
def countries(request):
    countriesdata = serialize('geojson', Countries.objects.all())
    return HttpResponse(countriesdata, content_type='json')