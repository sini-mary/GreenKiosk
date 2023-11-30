from django.shortcuts import render,redirect
from .forms import CartuploadForm
from Cartsystem.models import Cart
from inventory.models import Product
def upload_cart(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = CartuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CartuploadForm()
        
    return render(request, "cart/cart_list.html", {"form": form})

  
def cart_list(request):
     cart= Cart.objects.all()
     return render (request,"cart/cart_list.html",{"cart":cart})        
 
def  cart_detail(request,id):
  product = Product.objects.get(id =id)
  return render(request,"cart/cart_detail_view.html",{"product":product})
