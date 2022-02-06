from django.shortcuts import render
from .models import * 

def store(request):
	products = Product.objects.all()
	context = {'products':products}
	#print(products)
	return render(request, 'store_app/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0} # added here for unauth users
    context = {'items':items, 'order' : order}
    return render(request, 'store_app/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: #guest user
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0} # added here for unauth users
    context = {'items':items, 'order' : order}
    return render(request, 'store_app/checkout.html', context)