from myapp.models import Producto

class Cart():
    def __init__(self,request):
        self.session=request.session
        
        #Toma la session key si la hay
        cart=self.session.get('session_key')
        
        #Si el usuario es nuevo crea una key session
        if 'session_key' not in request.session:
            cart=self.session['session_key']= {}
            
            
        #Hay que asegurarse que cart esta disponible en todas la paginas
        self.cart=cart
        
    def add (self, producto, quantity):
        producto_id=str(producto.id)
        producto_qty=str(quantity)
        
        #logica
        if producto_id in self.cart:
            pass
        else:
            #self.cart[producto_id]={'precio':str(producto.precio)}
            self.cart[producto_id]=int(producto_qty)
        self.session.modified=True
        
        
    def __len__(self):
        return len(self.cart)
    
    def get_productos (self):
        #Toma los ids del carrito
        producto_ids =self.cart.keys()
        #usa los ids para ver los productos en la base de datos (models)
        productos=Producto.objects.filter(id__in=producto_ids)
        return productos
    def get_cantidad(self):
        cantidad=self.cart
        return cantidad