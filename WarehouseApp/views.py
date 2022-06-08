from django.shortcuts import render, redirect
from ProductApp.models import Product
from django.contrib.auth.decorators import login_required
from UserApp.models import *


@login_required(redirect_field_name='')
def index(request):
    print(request.session.get_expire_at_browser_close())
    biouser = BioUser.objects.get(user=request.user)
    products = Product.objects.filter(stock__lte = 50)
    nav_active = {
        'dashboard': 'active',
    }
    context = {
        'title': 'Dashboard',
        'menu_active': nav_active,
        'products': products,
        'biouser': biouser,
    }
    return render(request, 'dashboard.html', context)

def error_handler(request, exception):
    print(exception)
    return render(request, 'error_pages/404.html')

def error(request):
    context = {
        'title': '404 Forbiden',
    }
    return render(request, 'error_pages/404.html', context)

def new_user(request):
    biouser = BioUser.objects.get(user=request.user)
    context = {
        'title': 'Dashboard',
        'new_user': True,
        'bio_user': biouser,
    }
    return render(request, 'new_user.html', context)