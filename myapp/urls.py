from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('store', views.store, name="store"),
    path('sumar_producto',views.sumar_producto, name="sumar-producto"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('Register', views.Register_user, name="Register"),
    path('Productos/<int:pk>', views.Productos, name="producto"),
    path('categoria/<str:foo>', views.categoria, name="categoria"),
]
