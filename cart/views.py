from django.shortcuts import render, get_object_or_404
from .cart import Cart
from myapp.models import Producto
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    return render(request, "cart_summary.html",{})

def cart_add(request):
    #Get the cart
    cart= Cart(request)
    #test for post
    if request.POST.get('action')== 'post':
        #GET stuff
        producto_id= int(request.POST.get('producto.id'))
        #ver producto db
        product=get_object_or_404(Producto, id=producto_id)
        #guardar en la sesion
        cart.add(product=product)
        #return response
        response=JsonResponse({'Product name':product.nombre})
        return response
        


def cart_delete(request):
    return render(request, "cart_delete.html",{})

def cart_update(request):
    return render(request, "cart_update.html",{})