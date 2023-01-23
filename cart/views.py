from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from shop.models import *


# Create your views here.
def cart_details(request, tot=0, count=0, ct_items=None, t=0, shipping=0):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct)
        for i in ct_items:
            tot += (i.prodt.price * i.quantity)
            count += i.quantity
            t = tot
            if t <= 1499:
                shipping = 80
                t += shipping
            else:
                shipping = 0
                t += shipping
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 'tt': tot, 'cn': count, 't': t, 'sh': shipping})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prodt = products.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(prodt=prodt, cart=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity += 1
        c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(prodt=prodt, quantity=1, cart=ct)
        c_items.save()
    return redirect('cartDetails')


def min_cart(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prodt = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(prodt=prodt, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')


def cart_delete(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prodt = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(prodt=prodt, cart=ct)
    c_items.delete()
    return redirect('cartDetails')


# Create your views here.
