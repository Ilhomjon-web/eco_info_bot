from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_admin, name='redirect_admin'),
]