from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from cart.models import cartlist, items
from cart.views import c_id
from .models import *


# Create your views here.
def home(request, c_slug=None):
    # c_page = None
    # prod = None
    if c_slug is not None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prod = products.objects.filter(category=c_page, available=True)
    else:
        prod = products.objects.all().filter(available=True)
    cate = categ.objects.all()
    paginator = Paginator(prod, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'pr': prod, 'ct': cate, 'pg': pro})


def prodDetails(request, product_slug, c_slug):
    try:
        prod = products.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'detail.html', {'pr': prod})


def shop(request):
    prod = products.objects.all()
    paginator = Paginator(prod, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'shop.html', {'pr': prod, 'pg': pro})


# def cart(request, tot=0, count=0, ct_items=None):
#     return render(request, 'cart.html')


def checkout(request, tot=0, count=0, shipping=0, ct_items=None):
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

    return render(request, 'checkout.html', {'ci': ct_items, 'tt': tot, 'cn': count, 'sh': shipping, 't': t})


def contact(request):
    return render(request, 'contact.html', )


def search(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'pr': prod})
