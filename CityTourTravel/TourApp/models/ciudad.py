from django.db import models

class Ciudad(models.Model):
    ciu_nombre = models.CharField(primary_key=True, max_length=20, null=False, blank=False)
    ciu_pais = models.CharField(max_length=20, null=False, blank=False)