from django.urls import path

from .views import cart_add, cart_detail, cart_remove

app_name = "cart"

urlpatterns = [
    path("", cart_detail, name="detail"),
    path("add/<int:doacao_id>/", cart_add, name="add"),
    path("remove/<int:doacao_id>/", cart_remove, name="remove"),
]