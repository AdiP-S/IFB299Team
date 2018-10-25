from django.shortcuts import render
from .models import Customers_Rental, Orders, Rentaldatabase
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import UserProfile
from django.contrib.auth.models import User
from django.db.models import Count

#authentication
def type_check(user):
    return user.userprofile.user_type.startswith(('Employee','Manager'))

# View Home Page
def home(request):
    return render(request, 'rental/home.html')

# View About Page
def about(request):
    return render(request,'rental/about.html')

# View Checkout Page
def Checkout(request):
    return render(request,'rental/Checkout.html')

# View After Checkout Page
def CheckoutResult(request):
    return render(request,'rental/CheckoutResult.html')

# View viewVehicle Page
def viewVehicle(request):
    order = Rentaldatabase.objects.all()
    context = {
    'orders': order
    }
    return render(request, 'rental/viewVehicle.html', context)

# View Chart Page
@login_required
@user_passes_test(type_check, login_url = 'rental-home')

def chart(request):

    year05 = 0
    year06 = 0
    year07 = 0

    order05 = Rentaldatabase.objects.filter(order_pickupdate__startswith = '2005', pickup_store_state_name__iexact = request.user.userprofile.user_state)
    for item in order05:
        year05 = year05 + 1

    order06 = Rentaldatabase.objects.filter(order_pickupdate__startswith = '2006', pickup_store_state_name__iexact = request.user.userprofile.user_state)
    for item in order06:
        year06 = year06 + 1

    order07 = Rentaldatabase.objects.filter(order_pickupdate__startswith = '2007', pickup_store_state_name__iexact = request.user.userprofile.user_state)
    for item in order07:
        year07 = year07 + 1
    context = {'orders': year05, 'orders1': year06,  'orders2' : year07 }

    return render(request, 'rental/chart.html', context)


@login_required
@user_passes_test(type_check, login_url = 'rental-home')

def monthly_chart(request):

    year05 = 200507
    year2005 = []
    value05 = 0

    year06 = 200601
    year2006 = []
    value06 = 0

    year07 = 200701
    year2007 = []
    value07 = 0

    for x in range(6):
        order05 = Rentaldatabase.objects.filter(order_pickupdate__contains = str(year05), pickup_store_state_name__iexact = request.user.userprofile.user_state)
        value05 = 0
        for item in order05:
            value05 = value05 + 1
        year2005.append(value05)
        year05 = year05 + 1

    for x in range(12):
        order06 = Rentaldatabase.objects.filter(order_pickupdate__contains = str(year06),pickup_store_state_name__iexact = request.user.userprofile.user_state)
        value06 = 0
        for item in order06:
            value06 = value06 + 1
        year2006.append(value06)
        year06 = year06 + 1

    for x in range(2):
        order07 = Rentaldatabase.objects.filter(order_pickupdate__contains = str(year07), pickup_store_state_name__iexact = request.user.userprofile.user_state)
        value07 = 0
        for item in order07:
            value07 = value07 + 1
        year2007.append(value07)
        year07 = year07 + 1

    context = {'orders': year2005, 'orders1': year2006,  'orders2' : year2007 }

    return render(request, 'rental/chart_monthly.html', context)

# View order database page - requires the user to be logged in
@login_required
@user_passes_test(type_check, login_url = 'rental-home')

def database(request):
    context = {
        'orders': Rentaldatabase.objects.filter(pickup_store_state_name__iexact = request.user.userprofile.user_state)
    }
    return render(request, 'rental/database.html', context)

# View customer database page - Requires the user to be logged in
@login_required
@user_passes_test(type_check, login_url = 'rental-home')

def customer(request):
    context = {
        'customers': Customers_Rental.objects.filter(customer_occupation__iexact = "Labour")
    }
    return render(request, 'rental/customer.html', context)
# View vehicle database page - Requires the user to be logged in
@login_required
@user_passes_test(type_check, login_url = 'rental-home')

def vehicle(request):
    context = {
        'vehicles': Rentaldatabase.objects.filter(pickup_store_state_name__iexact = request.user.userprofile.user_state)
    }
    return render(request, 'rental/vehicle.html', context)
