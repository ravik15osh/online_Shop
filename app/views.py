from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Nike,Images,Order,OrderItem
from django.http import HttpResponseRedirect
import uuid
from django.contrib.auth.decorators import login_required



def str1(request):
    nike = Nike.objects.all()
    context = {'nike':nike}
    return render(request, 'index.html',context)

@login_required(login_url='/sign_up/')
def remove_from_cartpage(req,id):
    cart_products = req.session.get('cart_products', [])
    cart_products.remove(id)
    req.session['cart_products'] = cart_products
    return HttpResponseRedirect

 
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



@login_required(login_url='/sign_up/')
def cart(req, id):
    cart_products = req.session.get('cart_products', [])
    cart_products.append(id)
    st = (set(cart_products)) 
    req.session['cart_products'] = list(st)
    nike = Nike.objects.all()
    return HttpResponseRedirect('/')


def delete(req,id):
    cart_products = req.session.get('cart_products',[])
    cart_products.remove(id)
    req.session['cart_products'] = cart_products
    return HttpResponseRedirect('/')



@login_required(login_url='/sign_up/')
def cards(req):
    cart_products = req.session.get('cart_products', []) 
    cart_products = Nike.objects.filter(id__in = cart_products) 
    nike = Nike.objects.all()
    
    total_price = 0
    for i in nike:
        total_price += i.price
    context = {'nike':nike, 'amount':nike.count(), 'total_price':total_price,}
    return render(req,'cards.html',context)



def remove_from_cardpage(req, id):
    cart_products = req.session.get('cart_products', [])
    cart_products.remove(id)
    req.session['cart_products'] = cart_products
    return HttpResponseRedirect('/')







@login_required(login_url='/sign_up/')
def favorites_page(req):
    favorite_product = req.session.get('favorite_products', []) 
    favorite_products = Nike.objects.filter(id__in = favorite_product) 
    return render(req,'favorite.html',{'nike':favorite_products})






@login_required(login_url='/sign_up/')
def order(request):
    if request.method == 'POST':
        cart_product = request.session.get('cart_products',[])
        cart_products = Nike.objects.filter(id__in = cart_product)
        
        total_price = 0 
        for i in cart_products:
            total_price += i.price
            
            
        order = Order.objects.create(
        user = request.user,
        total_price = total_price,
        messege = request.POST.get('messege'),
        code = uuid.uuid4(),
        address = request.POST.get('address'),
        phone_number = request.POST.get('phone_number'),
        )
        
        
        for i in cart_products:
            item = OrderItem.objects.create(order=order,product=i)
            
            
        cart_products  = request.session.get('cart_products', [])
        cart_products = []
        request.session['cart_products'] = cart_products
    return render(request, 'order.html')
        
                
# def order(request):
#     return render(request,'order.html')        