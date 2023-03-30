from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Nike,Images
# Create your views here.


def str1(request):
    nike = Nike.objects.all()
    context = {'nike':nike}
    return render(request, 'index.html',context)

def detail(req):
    return render(req,'detail.html')
 
def detail(req, id):
    product = Nike.objects.get(id=id)
    images = Images.objects.filter(sneakers=product)
    return render(req, 'detail.html', {'product':product,'images':images}) 

def favorites(req, id):
    favorite_products = req.session.get('favorite_products', [])
    favorite_products.append(id)
    st = (set(favorite_products)) 
    req.session['favorite_products'] = list(st)
    nike = Nike.objects.all()
    context = {'nike':nike}
    print(st)
    return render(req,'index.html',context)

def favorites_page(req):
    favorite_product = req.session.get('favorite_products', []) 
    favorite_products = Nike.objects.filter(id__in = favorite_product) 
    return render(req,'favorite.html',{'nike':favorite_products})

def cards(req):
    card_product = req.session.get('card_products', []) 
    card_products = Nike.objects.filter(id__in = card_product) 
    return render(req,'cards.html',{'nike':card_products})

def addcart(req, id):
    addcart_products = req.session.get('addcart_products', [])
    addcart_products.append(id)
    st = (set(addcart_products)) 
    req.session['addcart_products'] = list(st)
    nike = Nike.objects.all()
    context = {'nike':nike}
    print(st)
    return render(req,'index.html',context)