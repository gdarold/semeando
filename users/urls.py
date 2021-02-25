from django.urls import path
from .models import User
from .views import CreateUser, UpdateUser, DeleteUser, profile

app_name = "users"


urlpatterns = [
    path('new/', CreateUser.as_view(model=User), name="new"),
    path('update/<int:pk>/', UpdateUser.as_view(model=User), name="update"),
    path('delete/<int:pk>/', DeleteUser.as_view(model=User), name="delete"),
    path('profile/', profile, name="profile"),
]
