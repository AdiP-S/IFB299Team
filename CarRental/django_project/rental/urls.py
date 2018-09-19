from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='rental-home'),
    path('about/', views.about, name='rental-about'),
    path('database/', views.database, name='rental-database'),
    path('database/customer', views.customer, name='customer-database'),
    path('database/vehicle', views.vehicle, name='vehicle-database'),
]
