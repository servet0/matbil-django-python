from django.shortcuts import render, redirect
from .models import Navbar, Navbar2, Home, Duyuru

def home(request):
    navbars = Navbar.objects.first()
    navbars2 = Navbar2.objects.all().order_by()
    homes = Home.objects.first()
    duyurus = Duyuru.objects.all().order_by('-date')

    context = {'navbars':navbars, 'navbars2': navbars2, 'homes':homes, 'duyurus': duyurus}

    return render(request, 'base/home.html', context)

# Create your views here.
