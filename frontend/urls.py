from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from .views import countries

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='static/index.html', permanent=False), name='index'),
    url(r'^countriesdata/', countries, name='countries'),

]