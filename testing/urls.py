from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='testing-home'),
    path('about/', views.about, name='testing-about'),
]