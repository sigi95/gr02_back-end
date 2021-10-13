from django.db import models

from .carrito import Carrito

class Compras(models.Model):
    com_id = models.AutoField(primary_key=True)
    usu_id = models.OneToOneField(Carrito, related_name='Com_id', on_delete=models.CASCADE)

    Metodo = [
        ('PayU','PayU'),
        ('Visa','Visa'),
        ('MC','Master Card'),
        ('AE','American Express'),
        ('DC','Diners Club'),
        ('PSE','Pagos Seguros en Línea'),
    ]

    Confirmar = [
        (1,'Sí'),
        (2,'No'),
        (3,'Por Confirmar'),
    ]

    com_metodoPago = models.CharField('Método Pago', choices=Metodo, max_length=40, null=False, blank=False)
    com_numeroCuenta = models.BigIntegerField('Número Cuenta',null=False)
    com_confirmarPago = models.CharField('Confirmar pago', choices=Confirmar, max_length=20, default='Por confirmar', null=True)
    com_fechaPago = models.DateTimeField('Fecha Pago', null=True, default='2021-01-02T00:00:00Z')

    def __int__(self):
        return self.usu_id