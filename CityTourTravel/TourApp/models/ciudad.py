from django.db import models

class Ciudad(models.Model):
    #ciu_id = models.AutoField(primary_key=True)
    ciu_nombre = models.CharField('Nombre ciudad', primary_key=True, max_length=20, null=False, blank=False)
    ciu_pais = models.CharField('Pais', max_length=20, null=False, blank=False)

    def __str__(self):
        return self.ciu_nombre