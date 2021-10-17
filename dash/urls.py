from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analytics/', views.charts, name='charts'),
    path('learning/', views.learning, name='learning')
]
