from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='rental-home'),
    path('about/', views.about, name='rental-about'),

]
