from django.urls import path
from . import views

urlpatterns = [
    #url path for home page
    path('', views.home, name ='rental-home'),
    #url path for about page
    path('about/', views.about, name='rental-about'),
    #url path for order database page
    path('database/', views.database, name='rental-database'),
    #url path for chart page
    path('chart/', views.chart, name='rental-chart'),
    #url path for monthly chart page
    path('monthly-chart/', views.monthly_chart, name='rental-monthly-chart'),
    #url path for customer database page
    path('database/customer', views.customer, name='customer-database'),
    #url path for vehicle database page
    path('database/vehicle', views.vehicle, name='vehicle-database'),
    #url path for view vehicle page
    path('viewVehicle/', views.viewVehicle, name='rental-viewVehicle'),
    
    path('Checkout/', views.Checkout, name='rental-Checkout'),

    path('CheckoutResult/', views.CheckoutResult, name='rental-CheckoutResult'),
]
