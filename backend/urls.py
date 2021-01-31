from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'countries', views.CountriesViewSet)
router.register(r'earthquakes', views.EarthquakesViewSet)


urlpatterns = [
    path('backend/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
]



