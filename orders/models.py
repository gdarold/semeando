from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from doacao.models import Doacao
from users.models import User


class Order(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    doacao = models.ForeignKey(Doacao,
                               related_name='order_items',
                               on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(settings.CART_ITEM_MAX_QUANTITY),
            MinValueValidator(1),
        ]
    )

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
