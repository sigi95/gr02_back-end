from django.db import models
from .ciudad import Ciudad

class Tour(models.Model):
    tour_id = models.BigAutoField(primary_key=True)
    tour_nombre = models.CharField('Nombre', max_length=60, null=False, blank=False)
    ciu_nombre = models.ForeignKey(Ciudad, related_name='Tour_ciudad', on_delete=models.CASCADE, null=False)
    tour_descripcion = models.CharField('Descripcion',max_length=250, null=False)
    tour_precio = models.FloatField('Precio',null=False)
    tour_fechaHoraInicio = models.DateTimeField('Fecha inicio',null=False, default='2021-01-01T00:00:00Z')
    tour_fechaHoraFin = models.DateTimeField('Fecha fin',null=False, default='2021-01-02T00:00:00Z')
    tour_duracionHoras = models.IntegerField('Duracion',null=False, blank=False)
    
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
    tour_transporte = models.CharField('Transporte',max_length=4, choices=Transporte, default='A pie', null=False)
    tour_alimentacion = models.CharField('Alimentacion',max_length=100, null=False)
    tour_hospedaje = models.CharField('Hospedaje',max_length=2, choices=Hospedaje, default='No', null=False)
    tour_kilometros = models.IntegerField('Kilometros',null=False)
    tour_inicio = models.CharField('Inicio',max_length=60, null=False)
    tour_fin = models.CharField('Fin',max_length=60, null=False)

    def __str__(self):
        return self.tour_nombre
