from django.urls import path
from . import views
from .views import search
from .views import home

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('search/', views.search),
    path('add/', views.add_employee),
    path('search/', search, name='search'),
    path('', home, name='home'),

]
