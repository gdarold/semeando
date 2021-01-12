from django.urls import path

from .views import ProductDetailView, ProductListView

app_name = "doacao"


urlpatterns =[
    path("", ProductListView.as_view(), name="list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("tipo_doacao/<slug:slug>/", ProductListView.as_view(), name="list_by_tipo_doacao"),

]