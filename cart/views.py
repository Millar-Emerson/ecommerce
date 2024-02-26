from django.shortcuts import render, get_object_or_404
from .cart import Cart
from myapp.models import Producto
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_productos=cart.get_productos
    cantidades=cart.get_cantidad
    carrito_total=cart.cart_total()
    return render(request, "cart_summary.html",{"cart_productos":cart_productos,
                                                "cantidades":cantidades,
                                                "carrito_total":carrito_total})

def cart_add(request):
    #Get the cart
    cart= Cart(request)
    #test for post
    if request.POST.get('action') == 'post':
        #GET stuff
        producto_id= int(request.POST.get('producto_id'))
        producto_qty=int(request.POST.get('producto_qty'))
        #ver producto db
        producto=get_object_or_404(Producto, id=producto_id)
        #guardar en la sesion
        cart.add(producto=producto, quantity=producto_qty)
        
        #Get Cart Quantity
        cart_quantity=cart.  __len__()
        #return response
        #response=JsonResponse({'Producto nombre':producto.nombre})
        messages.success(request,("El Producto se añadio al carrito"))
        response=JsonResponse({'cantidad':cart_quantity})
        return response
        


def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        #GET stuff
        producto_id= int(request.POST.get('producto_id'))
        cart.delete(producto=producto_id)
        response=JsonResponse({'producto': producto_id})
        return response 

def cart_update(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        #GET stuff
        producto_id= int(request.POST.get('producto_id'))
        producto_qty=int(request.POST.get('producto_qty'))
        
        cart.update(producto=producto_id, quantity=producto_qty)
        
        messages.success(request,("Se actualizo el carrito"))
        response=JsonResponse({'qty': producto_qty})
        return response 