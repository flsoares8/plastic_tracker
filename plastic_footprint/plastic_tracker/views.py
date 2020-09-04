from django.shortcuts import render, redirect
from .forms import CustomerForm, ProductForm
from .models import Customer, Product

# Create your views here.


def landing_page(request):
    return render(request, "plastic_tracker/landing_page.html")


def customer_registration(request):
    if request.method == "GET":
        form = CustomerForm()
        return render(request, "plastic_tracker/customer_registration.html", {'form': form})
    else:
        # if it is a POST, save the POST data
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

def customer_info(request, id):
    context = {'customer_info': Customer.objects.get(pk=id)}
    return render(request, "plastic_tracker/customer_info.html", context)

def product_registration(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "plastic_tracker/product_registration.html", {'form': form})
    else:
        # if it is a POST, save the POST data
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
