from django.shortcuts import render, redirect
from .models import Producto, Categoria
from .forms import ProductoForm, SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



def Productos (request,pk):
    producto= Producto.objects.get(id=pk)
    return render(request, 'store/Producto.html', {'producto': producto})


def categoria(request,foo):
    foo=foo.replace('-',' ')
    #Toma la categoria desde el url
    try:
        categoria=Categoria.objects.get(name=foo)
        producto=Producto.objects.filter(categoria=categoria)
        return render(request, 'categoria.html', {'producto':producto,'categoria':categoria})
    except:
        messages.success(request,("Esa categoria no existe"))
        return redirect('home')

def sumar_producto(request):
    submitted= False
    if request.method == "POST":
        form= ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sumar_producto?submitted=True')
    else:
        form= ProductoForm
        if 'submitted' in request.GET:
            submitted=True
        
    return render(request, 'store/sumar_producto.html', {'form':form, submitted:'submitted'})

def home(request):
    lista_producto= Producto.objects.all()
    return render(request, 'store/home.html', {'lista_producto': lista_producto})

def store(request):
    lista_producto= Producto.objects.all()
    return render(request, 'store/store.html', {'lista_producto': lista_producto})

def logout_user(request):
    logout(request)
    return redirect('home') 


def login_user(request):
    if request.method== "POST": 
        username= request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("Te logeaste"))
            return redirect("home")
        
        else:
            messages.success(request,("No te logeaste"))
            return redirect("login")
    else:
        
        return render(request, 'store/login.html', {})
    
def Register_user (request):
    form=SignUpForm()
    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #log in user
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,("Te registraste"))
            return redirect("home")
        else:
            messages.success(request,("No te registraste"))
            return redirect("Register")
    else:   
        return render(request, 'store/Register.html', {'form':form})

