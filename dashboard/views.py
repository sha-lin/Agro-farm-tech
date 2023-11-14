from django.shortcuts import render, redirect
from .models import Product, Request
from .forms import ProductForm


def dashboard(request):
    products = Product.objects.filter(farmer=request.user)
    requests = Request.objects.filter(product__farmer=request.user)
    return render(request, 'tfarmapp/dashboard.html', {'products': products, 'requests': requests})

def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'tfarmapp/post_product.html', {'form': form})

def view_requests(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'tfarmapp/view_requests.html', {'products': products})