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
        
    def add(self, producto):
        product_id=str(producto.id)
        
        #logica
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]={'precio':str(producto.precio)}
        self.session.modified=True