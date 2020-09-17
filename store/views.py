from django.shortcuts import render

# Create your views here.

def store(request):
    ctx = {}
    return render(request, 'store/store.html', ctx)

def cart(request):
    ctx = {}
    return render(request, 'store/cart.html', ctx)

def checkout(request):
    ctx = {}
    return render(request, 'store/checkout.html', ctx)


