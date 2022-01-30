from django.shortcuts import render

# Create your views here.
def store(request):
	context = {}
	return render(request, 'store_app/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store_app/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store_app/checkout.html', context)