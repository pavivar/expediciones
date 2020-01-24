from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    #  orders = Order.objects.all()
    orders = Order.objects.filter(delegacion=request.user)
    return render(request, 'index.html', {'orders': orders})


@login_required
def show(request, order_id):
    order = Order.objects.filter(id=order_id)
    return render(request, 'show.html', {'order': order})


@login_required
def new(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request,
                                'Se ha creado un nuevo pedido.',
                                'alert-success'))
            else:
                return redirect('/', messages.error(request, 
                                'No se ha grabado el pedido', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 
                            'Hay errores en el formulario', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new.html', {'form':form})


@login_required
def edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request,
                                'El pedido se ha actualizado correctamente.',
                                'alert-success'))
            else:
                return redirect('/', messages.error(request,
                                'No se han guardado las modificaciones', 'alert-danger'))
        else:
            return redirect('/', messages.error(request,
                            'Hay errores en el formulario', 'alert-danger'))
    else:
        form = OrderForm(instance=order)
        return render(request, 'edit.html', {'form': form})


@login_required
def destroy(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/', messages.success(request,
                    'El pedido se ha borrado correctamente.', 'alert-success'))
