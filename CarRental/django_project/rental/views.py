from django.shortcuts import render
from .models import Customers_Rental
#from .models import Customers


# Create your views here.
def home(request):
    context = {
        'customers': Customers_Rental.objects.all()
    }
    return render(request, 'rental/home.html', context)

def about(request):
    return render(request,'rental/about.html')
