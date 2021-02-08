from django.urls import path

from .views import DoacaoDetailView, DoacaoListView, DoacaoCreate, DoacaoUser

app_name = "doacao"


urlpatterns =[
    path("", DoacaoListView.as_view(), name="list"),
    path('new/', DoacaoCreate.as_view(), name='new'),
    path("<slug:slug>/", DoacaoDetailView.as_view(), name="detail"),
    path("tipo_doacao/<slug:slug>/", DoacaoListView.as_view(), name="list_by_tipo_doacao"),
    path("minhas_doacoes/", DoacaoUser.as_view(), name="list_by_minhas_doacoes"),

]