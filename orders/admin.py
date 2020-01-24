from django.contrib import admin
from .models import Order


# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('obra', 'usuario', 'num_pedido', 'fecha_pedido',
                    'fecha_entrega', 'delegacion', 'producto_id', 'cantidad',
                    'descripcion', 'estado_pedido')
    list_filter = ('usuario', 'num_pedido', 'fecha_entrega', 'estado_pedido')
    ordering = ('fecha_entrega', 'estado_pedido')
    search_fields = ('num_pedido', 'delegacion')
    date_hierarchy = ('fecha_entrega')
