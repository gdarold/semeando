from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from doacao.models import Doacao

from .cart import Cart
from .forms import CartAddDoacaoForm


@require_POST
def cart_add(request, doacao_id):
    cart = Cart(request)
    doacao = get_object_or_404(Doacao, id=doacao_id)

    form = CartAddDoacaoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            doacao=doacao, quantidade=cd["quantidade"], override_quantidade=cd["override"]
        )

    return redirect("cart:detail")


@require_POST
def cart_remove(request, doacao_id):
    cart = Cart(request)
    doacao = get_object_or_404(Doacao, id=doacao_id)
    cart.remove(doacao)
    return redirect("cart:detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", {"cart": cart})
