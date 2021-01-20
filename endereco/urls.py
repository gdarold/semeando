from django.conf.urls import url
from django.urls import path

from endereco.views import\
    EnderecoCreate, \
    EnderecoDelete, \
    EnderecoList, \
    EnderecoEdit

app_name = "endereco"


urlpatterns = [

    path('new/', EnderecoCreate.as_view(), name='new'),
    path('list/', EnderecoList.as_view(), name='list'),
    path('update/<int:pk>/', EnderecoEdit.as_view(), name='edit'),
    path('delete/<int:pk>/', EnderecoDelete.as_view(), name='del'),
]
