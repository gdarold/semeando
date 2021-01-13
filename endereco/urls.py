from django.urls import path

from endereco.views import EnderecoListView, EnderecoDetailView

app_name = "endereco"


urlpatterns =[
    path("", EnderecoListView.as_view(), name="list"),
    path("<slug:slug>/", EnderecoDetailView.as_view(), name="detail"),
    path("tipo_doacao/<slug:slug>/", EnderecoListView.as_view(), name="list_by_tipo_doacao"),
]