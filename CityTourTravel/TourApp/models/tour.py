from django.db import models
from .ciudad import Ciudad

class Tour(models.Model):
    tour_nombre = models.CharField(primary_key=True, max_length=60, null=False, blank=False)
    ciu_nombre = models.ForeignKey(Ciudad, related_name='Tour_ciudad', on_delete=models.CASCADE)
    tour_descripcion = models.CharField(max_length=250, null=False)
    tour_precio = models.FloatField(null=False)
    tour_fechaHoraInicio = models.DateTimeField(null=False, default='2021-01-01T00:00:00Z')
    tour_fechaHoraFin = models.DateTimeField(null=False, default='2021-01-02T00:00:00Z')
    tour_duracionHoras = models.IntegerField(null=False, blank=False)
    
    Transporte = [
        ('PIE','A pie'),
        ('BICI','Bicicleta'),
        ('MOTO','Moto'),
        ('BUS','Bus'),
        ('CAR','Carro'),
        ('LAN','Lancha'),
        ('BAR','Barco'),
        ('AV','Avion')
    ]
    Hospedaje = [
        (1,'Si'),
        (2,'No')
    ]
    tour_transporte = models.CharField(max_length=4, choices=Transporte, default='A pie', null=False)
    tour_alimentacion = models.CharField(max_length=100, null=False)
    tour_hospedaje = models.CharField(max_length=2, choices=Hospedaje, default='No', null=False)
    tour_kilometros = models.IntegerField(null=False)
    tour_inicio = models.CharField(max_length=60, null=False)
    tour_fin = models.CharField(max_length=60, null=False)

    def __str__(self):
        return self.tour_nombre
