from django.db import models
import datetime

class Categoria (models.Model):
    nombre= models.CharField('Nombre Categoria', max_length=120)  
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre= models.CharField('Nombre Usuario', max_length=120)
    Apellido= models.CharField ('Apellido Usuario', max_length=120)
    email=models.EmailField('Email', max_length=120)
    contraseña=models.CharField('contraseña', max_length=120)
    celular=models.CharField(default='', blank=True, max_length=50)
    def __str__(self):
        return f'{self.nombre} {self.Apellido}'
    
    
class Producto (models.Model):
    nombre= models.CharField('Nombre Producto', max_length=120)
    precio=models.DecimalField(default=0, decimal_places=2, max_digits=6)
    descripcion=models.TextField(blank=True, default='',max_length=250, null=True)
    categorias=models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    imagen= models.ImageField(upload_to='images/')
    #Descuentos
    Esta_en_Descuento=models.BooleanField(default=False)
    Precio_Descuento=models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
    def __str__(self):
        return self.nombre  
    
    
class Orden (models.Model):
    producto=models.ForeignKey(Producto , on_delete=models.CASCADE)
    usuario= models.ForeignKey(Usuario , on_delete=models.CASCADE)
    cantidad= models.IntegerField(default=1)
    direccion=models.CharField(max_length=150, default='', blank=True)
    celular= models.CharField( default='', blank=True, max_length=50)
    fecha= models.DateField(default=datetime.datetime.today)
    estado= models.BooleanField(default=False)

    def __str__(self):
        return self.producto


