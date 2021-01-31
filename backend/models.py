from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Countries(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    name_long = models.CharField(max_length=254, blank=True, null=True)
    formal_en = models.CharField(max_length=254, blank=True, null=True)
    sov_a3 = models.CharField(max_length=254, blank=True, null=True)
    postal = models.CharField(max_length=254, blank=True, null=True)
    abbrev = models.CharField(max_length=254, blank=True, null=True)
    continent = models.CharField(max_length=254, blank=True, null=True)
    region_un = models.CharField(max_length=254, blank=True, null=True)
    subregion = models.CharField(max_length=254, blank=True, null=True)
    region_wb = models.CharField(max_length=254, blank=True, null=True)
    pop_est = models.BigIntegerField(blank=True, null=True)
    pop_rank = models.BigIntegerField(blank=True, null=True)
    gdp_md_est = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    pop_year = models.BigIntegerField(blank=True, null=True)
    lastcensus = models.BigIntegerField(blank=True, null=True)
    gdp_year = models.BigIntegerField(blank=True, null=True)
    economy = models.CharField(max_length=254, blank=True, null=True)
    income_grp = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Earthquakes(models.Model):
    gid = models.AutoField(primary_key=True)
    date = models.CharField(max_length=254, blank=True, null=True)
    time = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    depth = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    depth_erro = models.DecimalField(db_column='depth erro', max_digits=65535, decimal_places=2, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    depth_seis = models.DecimalField(db_column='depth seis', max_digits=65535, decimal_places=2, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    magnitude = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    magnitud_1 = models.CharField(max_length=254, blank=True, null=True)
    magnitud_2 = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    magnitud_3 = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    azimuthal = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    horizontal = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    horizont_1 = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    root_mean = models.DecimalField(db_column='root mean', max_digits=65535, decimal_places=2, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    id = models.CharField(max_length=254, blank=True, null=True)
    source = models.CharField(max_length=254, blank=True, null=True)
    location_s = models.CharField(db_column='location s', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    magnitud_4 = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'earthquakes'