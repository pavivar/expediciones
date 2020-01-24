from django.forms import ModelForm
from django import forms
from .models import Order
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(ModelForm):
    OPTIONS = (
        ('', ''),
        ('Granada', 'Granada'),
        ('Galicia', 'Galicia'),
        ('Zaragoza', 'Zaragoza')
    )
    OPTIONS2 = (
        ('Recibido', 'Recibido'),
        ('Preparado', 'Preparado'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
        ('Devuelto', 'Devuelto'),
        ('Cancelado', 'Cancelado')
    )
    estado_pedido = forms.TypedChoiceField(required=False, choices=OPTIONS2,
                                           widget=forms.RadioSelect)
    #  delegacion = forms.ChoiceField(choices=OPTIONS)
    #  fecha_pedido = forms.DateField(label=('Fecha pedido'),
    #                                 widget=forms.DateInput(
    #                                 format="%m/%d/%Y"))
    #  fecha_pedido = forms.DateField(input_formats=["%d %b %Y %H:%M:%S %Z"])

    fecha_pedido = forms.DateField(widget=forms.SelectDateWidget,
                                   initial=datetime.date.today)
    fecha_entrega = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Order
        fields = ['obra', 'usuario', 'num_pedido', 'fecha_pedido',
                  'fecha_entrega', 'delegacion', 'producto_id', 'cantidad',
                  'descripcion', 'estado_pedido']
        # widgets = {'fecha_pedido':
        #           forms.DateInput(format=('%d-%m-%Y'),
        #                          attrs={'class': 'form-control',
        #                                 'placeholder': 'Select a date',
        #                                  'type': 'date'})}
