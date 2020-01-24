from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Order (models.Model):
    DELEGACIONES = (
        ('', ''),
        ('Granada', 'Granada'),
        ('Galicia', 'Galicia'),
        ('Zaragoza', 'Zaragoza')
    )
    ESTADOS = (
        ('Recibido', 'Recibido'),
        ('Preparado', 'Preparado'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
        ('Devuelto', 'Devuelto'),
        ('Cancelado', 'Cancelado')
    )
    obra = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='expediciones_pedidos')
    num_pedido = models.CharField(max_length=200)
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()
    delegacion = models.CharField(max_length=200,
                                  choices=DELEGACIONES)
    producto_id = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    estado_pedido = models.CharField(max_length=50,
                                     choices=ESTADOS,
                                     default='Recibido')


class Meta:
    ordering = ('fecha_entrega')


def __str__(self):
    return self.usuario
