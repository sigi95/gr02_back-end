from django.db import models

from .usuario import User
from .tour import Tour

class Carrito(models.Model):
    cc_id = models.BigAutoField(primary_key=True)
    cc_usu_nombreUsuario = models.ForeignKey(User, max_length=60, related_name='Carrito_usuario', on_delete=models.CASCADE)
    cc_tour_nombre = models.ForeignKey(Tour, max_length=60, related_name='Carrito_tour', on_delete=models.CASCADE)
    cc_numeroPersonas = models.IntegerField('Numero personas', null=False)
    cc_precioTotal = models.FloatField('Precio total', null=False)