from django.urls import path, include
from crud import views

urlpatterns = [
    path('', views.home)
]
