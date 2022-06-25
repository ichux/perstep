# pages/urls.py
from django.urls import path

from .views import AboutPageView, HomePageView, home_page_view

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("hp", home_page_view, name="hp-home"),
]
