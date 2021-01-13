from django.urls import path

from .views import DoacaoDetailView, DoacaoListView

app_name = "doacao"


urlpatterns =[
    path("", DoacaoListView.as_view(), name="list"),
    path("<slug:slug>/", DoacaoDetailView.as_view(), name="detail"),
    path("tipo_doacao/<slug:slug>/", DoacaoListView.as_view(), name="list_by_tipo_doacao"),

]