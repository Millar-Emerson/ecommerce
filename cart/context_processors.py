from .cart import Cart

#Crear un context processors asi nuestro carrito funciona en todas las paginas
def cart(request):
    return{'cart':Cart(request)}