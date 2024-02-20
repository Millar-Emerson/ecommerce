from django.contrib import admin
from .models import Usuario
from .models import Producto
from .models import Orden
from .models import Categoria


admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(Categoria)
