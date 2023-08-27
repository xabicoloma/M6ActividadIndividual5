from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# Create your views here.

def bienvenida(request):
    return render(request,'home/index.html')

@login_required
def home(request):
    return render(request,'home/home.html')


@login_required
def staffPage(request):
    lista_usuario = User.objects.all()
    return render(request,'home/restricted_page.html', {
        'lista_usuario' : lista_usuario
    })

@login_required
def mostrarUsuario(request):
    lista_usuario = User.objects.all()
    return render(request, 'home/mostrar_usuario.html', {
        'lista_usuario' : lista_usuario
    })

@login_required
def logout(request):
    logout(request)

def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            username = formulario_p.cleaned_data["username"]
            print(username)
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
            formulario_p.save()
            return redirect('blog')
        else:
            messages.error(request, "Hubo un error en el registro")
    formulario = RegistroUsuarioForm()
    return render(request, 'home/registro.html', {'formulario': formulario})

