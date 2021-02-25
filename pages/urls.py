from django.urls import path

from .views import AboutPageView, HomePageView, contact_page


app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", contact_page, name="contact"),

]