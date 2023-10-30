
from django.urls import path
from body import views

urlpatterns = [
    path('', views.home, name="home"),
]
