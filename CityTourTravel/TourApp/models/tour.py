from django.db import models
from .ciudad import Ciudad

class Tour(models.Model):
    tour_nombre = models.CharField(primary_key=True, max_length=60, null=False, blank=False)
    ciu_nombre = models.ForeignKey(Ciudad, related_name='Tour_ciudad', on_delete=models.CASCADE)
    tour_descripcion = models.CharField(max_length=250, null=False)
    tour_precio = models.CharField(max_length=8, null=False)
    tour_fechaHoraInicio = models.DateTimeField(null=False, default='01/01/2021 00:00:00')
    tour_fechaHoraFin = models.DateTimeField(null=False, default='02/01/2021 00:00:00')
    tour_duracionHoras = models.IntegerField(null=False, blank=False)
    #mediante una tupla creo las opciones a escoger en el campo de transporte
    #al igual para hospedaje
    Transporte = [
        (1,'A pie'),
        (2,'Bicicleta'),
        (3,'Moto'),
        (4,'Bus'),
        (5,'Carro'),
        (6,'Lancha'),
        (7,'Barco'),
        (8,'Avion')
    ]
    Hospedaje = [
        (1,'Si'),
        (2,'No')
    ]
    tour_transporte = models.CharField(max_length=1, choices=Transporte, default=Transporte[0])
    tour_alimentacion = models.CharField(max_length=100, null=False)
    tour_hospedaje = models.CharField(max_length=1, choices=Hospedaje, default=Hospedaje[1], null=False)
    tour_kilometros = models.IntegerField(null=False)
    tour_inicio = models.CharField(max_length=60, null=False)
    tour_fin = models.CharField(max_length=60, null=False)
