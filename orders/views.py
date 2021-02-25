from django.shortcuts import render
from django.shortcuts import get_object_or_404
from cart.cart import Cart
from endereco.models import Endereco
from users.models import User

from .models import OrderItem, Order
from .forms import OrderCreateForm


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            order = form.save()

            for item in cart:

                OrderItem.objects.create(order=order,
                                         doacao=item['doacao'],
                                         price=item['peso'],
                                         quantity=item['quantidade'])
            # clear the cart



            cart.clear()

            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    user = User.objects.get(username = order.usuario)
    endereco = Endereco.objects.get(usuario=user)

    return render(request,
                  'orders/order/detail.html',
                  {'order': order, 'user':user, 'endereco':endereco})

