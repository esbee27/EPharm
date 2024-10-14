from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm, ProductForm
from .models import Product


# Create your views here.
def index(request):
    return render(request, 'customer/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'customer/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'customer/login.html', {'form': form})


def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_page')
    else:
        form = ProductForm()
    return render(request, 'customer/upload_product.html', {'form': form})

def product_page(request):
    products = Product.objects.all()
    return render(request, 'customer/product_page.html', {'products': products})


def order(request):
    return render(request, 'customer/order.html')