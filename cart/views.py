from django.shortcuts import render, get_object_or_404
from .cart import Cart
from myapp.models import Producto
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_productos=cart.get_productos
    return render(request, "cart_summary.html",{"cart_productos":cart_productos})

def cart_add(request):
    #Get the cart
    cart= Cart(request)
    #test for post
    if request.POST.get('action')== 'post':
        #GET stuff
        producto_id= int(request.POST.get('producto_id'))
        #ver producto db
        producto=get_object_or_404(Producto, id=producto_id)
        #guardar en la sesion
        cart.add(producto=producto)
        
        #Get Cart Quantity
        cart_quantity=cart.  __len__()
        #return response
        #response=JsonResponse({'Producto nombre':producto.nombre})
        response=JsonResponse({'cantidad':cart_quantity})
        return response
        


def cart_delete(request):
    return render(request, "cart_delete.html",{})

def cart_update(request):
    return render(request, "cart_update.html",{})