import copy
from decimal import Decimal

from django.conf import settings
from doacao.models import Doacao

from .forms import CartAddDoacaoForm


class Cart:
    def __init__(self, request):
        if request.session.get(settings.CART_SESSION_ID) is None:
            request.session[settings.CART_SESSION_ID] = {}

        self.cart = request.session[settings.CART_SESSION_ID]
        self.session = request.session

    def __iter__(self):
        cart = copy.deepcopy(self.cart)

        doacoes = Doacao.objects.filter(id__in=cart)
        for doacao in doacoes:
            cart[str(doacao.id)]["doacao"] = doacao

        for item in cart.values():
            item["peso"] = Decimal(item["peso"])
            item["total_peso"] = item["quantidade"] * item["peso"]
            item["update_quantidade_form"] = CartAddDoacaoForm(
                initial={"quantidade": item["quantidade"], "override": True}
            )

            yield item

    def __len__(self):
        return sum(item["quantidade"] for item in self.cart.values())

    def add(self, doacao, quantidade=1, override_quantidade=False):
        doacao_id = str(doacao.id)

        if doacao_id not in self.cart:
            self.cart[doacao_id] = {
                "quantidade": 0,
                "peso": str(doacao.peso),
            }

        if override_quantidade:
            self.cart[doacao_id]["quantidade"] = quantidade
        else:
            self.cart[doacao_id]["quantidade"] += quantidade

        self.cart[doacao_id]["quantidade"] = min(20, self.cart[doacao_id]["quantidade"])

        self.save()

    def remove(self, doacao):
        doacao_id = str(doacao.id)

        if doacao_id in self.cart:
            del self.cart[doacao_id]
            self.save()

    def get_total_peso(self):
        return sum(
            Decimal(item["peso"]) * item["quantidade"] for item in self.cart.values()
        )

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
