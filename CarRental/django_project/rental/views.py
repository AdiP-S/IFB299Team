from django.shortcuts import render
from .models import Customers_Rental, Orders, Rentaldatabase
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
#from .models import Customers


# Create your views here.
def home(request):
    return render(request, 'rental/home.html')

def about(request):
    return render(request,'rental/about.html')

@login_required
def database(request):
    context = {
        'orders': Rentaldatabase.objects.filter(pickup_store_state_name__iexact = "New South Wales")
    }
    return render(request, 'rental/database.html', context)

@login_required
def customer(request):
    context = {
        'customers': Customers_Rental.objects.filter(customer_occupation__iexact = "Labour")
    }
    return render(request, 'rental/customer.html', context)

@login_required
def vehicle(request):
    context = {
        'vehicles': Rentaldatabase.objects.filter(pickup_store_state_name__iexact = "New South Wales")
    }
    return render(request, 'rental/vehicle.html', context)
