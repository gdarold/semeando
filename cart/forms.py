from django import forms
from django.conf import settings

DOACAO_QUANTIDADE_CHOICES = [
    (i, str(i)) for i in range(1, settings.CART_ITEM_MAX_QUANTITY + 1)
]


class CartAddDoacaoForm(forms.Form):
    quantidade = forms.TypedChoiceField(
        label="Quantidade", choices=DOACAO_QUANTIDADE_CHOICES, coerce=int
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
