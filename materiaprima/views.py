from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProduccinForm, materiaprimaForm, InventarioForm, EntradaForm, SalidaForm
from .models import Produccin, materiaprima, Inventario, Entrada, Salida
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('materiaprima')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })

@login_required
def inventario(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventario.html', {'inventarios': inventarios})

@login_required
def inventario_detail(request, inventario_id):
    if request.method == 'GET':
        inventario = get_object_or_404(Inventario, pk=inventario_id, user=request.user)
        form = InventarioForm(instance=inventario)
        return render(request, 'inventario_detail.html', {'inventario': inventario, 'form': form})
    else:
        try:
            inventario = get_object_or_404(Inventario, pk=inventario_id, user=request.user)
            form = InventarioForm(request.POST, instance=inventario)
            form.save()
            return redirect('inventario')
        except ValueError:
            return render(request, 'inventario_detail.html', {'inventario': inventario, 'form': form,
            'error': 'Error actualizando el registro'})

@login_required
def create_inventario(request):
    if request.method == 'GET':
        return render(request, 'create_inventario.html', {
        'form': InventarioForm
        })
    else: 
        try:
            form = InventarioForm(request.POST)
            new_inventario = form.save(commit=False)
            new_inventario.user = request.user
            new_inventario.save()
            return redirect('inventario')
        except ValueError:
            return render(request, 'create_inventario.html', {
                'form': ProduccinForm,
                'error': 'Agrega datos válidos'
            })

@login_required
def delete_inventario(request, inventario_id):
    inventario = get_object_or_404(Inventario, pk=inventario_id, user=request.user)
    if request.method == 'POST':
        inventario.delete()
        return redirect('inventario')

@login_required
def searchi(request):
    businv = request.GET["businv"]
    inventarios = Inventario.objects.filter(categoria__icontains=businv)
    return render(request, 'inventario.html', {'inventarios': inventarios})

@login_required
def entrada(request):
    entradas = Entrada.objects.order_by('-fecha')
    return render(request, 'entrada.html', {'entradas': entradas})

@login_required
def create_entrada(request):
    if request.method == 'GET':
        return render(request, 'create_entrada.html', {
        'form': EntradaForm
        })
    else: 
        try:
            form = EntradaForm(request.POST)
            new_entrada = form.save(commit=False)
            new_entrada.user = request.user
            new_entrada.save()
            return redirect('entrada')
        except ValueError:
            return render(request, 'create_entrada.html', {
                'form': EntradaForm,
                'error': 'Agrega datos válidos'
            })

@login_required
def entrada_detail(request, entrada_id):
    if request.method == 'GET':
        entrada = get_object_or_404(Entrada, pk=entrada_id, user=request.user)
        form = EntradaForm(instance=entrada)
        return render(request, 'entrada_detail.html', {'entrada': entrada, 'form': form})
    else:
        try:
            entrada = get_object_or_404(Entrada, pk=entrada_id, user=request.user)
            form = EntradaForm(request.POST, instance=entrada)
            form.save()
            return redirect('entrada')
        except ValueError:
            return render(request, 'entrada_detail.html', {'entrada': entrada, 'form': form,
            'error': 'Error actualizando el registro'})

@login_required
def delete_entrada(request, entrada_id):
    entrada = get_object_or_404(Entrada, pk=entrada_id, user=request.user)
    if request.method == 'POST':
        entrada.delete()
        return redirect('entrada')

@login_required
def searche(request):
    busent = request.GET["busent"]
    entradas = Entrada.objects.filter(fecha__icontains=busent)
    return render(request, 'entrada.html', {'entradas': entradas})

@login_required
def salida(request):
    salidas = Salida.objects.order_by('-fecha')
    return render(request, 'salida.html', {'salidas': salidas})

@login_required
def create_salida(request):
    if request.method == 'GET':
        return render(request, 'create_salida.html', {
        'form': SalidaForm
        })
    else: 
        try:
            form = SalidaForm(request.POST)
            new_salida = form.save(commit=False)
            new_salida.user = request.user
            new_salida.save()
            return redirect('salida')
        except ValueError:
            return render(request, 'create_salida.html', {
                'form': SalidaForm,
                'error': 'Agrega datos válidos'
            })

@login_required
def salida_detail(request, salida_id):
    if request.method == 'GET':
        salida = get_object_or_404(Salida, pk=salida_id, user=request.user)
        form = SalidaForm(instance=salida)
        return render(request, 'salida_detail.html', {'salida': salida, 'form': form})
    else:
        try:
            salida = get_object_or_404(Salida, pk=salida_id, user=request.user)
            form = SalidaForm(request.POST, instance=salida)
            form.save()
            return redirect('salida')
        except ValueError:
            return render(request, 'salida_detail.html', {'salida': salida, 'form': form,
            'error': 'Error actualizando el registro'})

@login_required
def delete_salida(request, salida_id):
    salida = get_object_or_404(Salida, pk=salida_id, user=request.user)
    if request.method == 'POST':
        salida.delete()
        return redirect('salida')

@login_required
def searchs(request):
    bussal = request.GET["bussal"]
    salidas = Salida.objects.filter(fecha__icontains=bussal)
    return render(request, 'salida.html', {'salidas': salidas})

@login_required
def Materiaprima(request):
    materiaprimas = materiaprima.objects.order_by('-fecha')
    return render(request, 'Materiaprima.html', {'materiaprimas': materiaprimas})

@login_required
def create_materiaprima(request):
    if request.method == 'GET':
        return render(request, 'create_materiaprima.html', {
        'form': materiaprimaForm
        })
    else: 
        try:
            form = materiaprimaForm(request.POST)
            new_materiaprima = form.save(commit=False)
            new_materiaprima.user = request.user
            new_materiaprima.save()
            return redirect('materiaprima')
        except ValueError:
            return render(request, 'create_materiaprima.html', {
                'form': ProduccinForm,
                'error': 'Agrega datos válidos'
            })

@login_required
def materiaprima_detail(request, materiaprima_id):
    if request.method == 'GET':
        mate = get_object_or_404(materiaprima, pk=materiaprima_id, user=request.user)
        form = materiaprimaForm(instance=mate)
        return render(request, 'materiaprima_detail.html', {'mate': mate, 'form': form})
    else:
        try:
            mate = get_object_or_404(materiaprima, pk=materiaprima_id, user=request.user)
            form = materiaprimaForm(request.POST, instance=mate)
            form.save()
            return redirect('materiaprima')
        except ValueError:
            return render(request, 'materiaprima_detail.html', {'mate': mate, 'form': form,
            'error': 'Error actualizando el registro'})

@login_required
def delete_materiaprima(request, materiaprima_id):
    mate = get_object_or_404(materiaprima, pk=materiaprima_id, user=request.user)
    if request.method == 'POST':
        mate.delete()
        return redirect('materiaprima')

@login_required
def search(request):
    buspro = request.GET["buspro"]
    materiaprimas = materiaprima.objects.filter(proveedor__icontains=buspro)
    return render(request, 'Materiaprima.html', {'materiaprimas': materiaprimas})

@login_required
def produccin(request):
    produccins = Produccin.objects.order_by('-fecha')
    return render(request, 'produccin.html', {'produccins': produccins})

@login_required
def create_produccin(request):

    if request.method == 'GET':
        return render(request, 'create_produccin.html', {
        'form': ProduccinForm
        })
    else: 
        try:
            form = ProduccinForm(request.POST)
            new_produccion = form.save(commit=False)
            new_produccion.user = request.user
            new_produccion.save()
            return redirect('produccion')
        except ValueError:
            return render(request, 'create_produccin.html', {
                'form': ProduccinForm,
                'error': 'Agrega datos válidos'
            })

@login_required
def produccion_detail(request, produccin_id):
    if request.method == 'GET':
        produccin = get_object_or_404(Produccin, pk=produccin_id, user=request.user)
        form = ProduccinForm(instance=produccin)
        return render(request, 'produccion_detail.html', {'produccin': produccin, 'form': form})
    else:
        try:
            produccin = get_object_or_404(Produccin, pk=produccin_id, user=request.user)
            form = ProduccinForm(request.POST, instance=produccin)
            form.save()
            return redirect('produccion')
        except ValueError:
            return render(request, 'produccion_detail.html', {'produccin': produccin, 'form': form,
            'error': 'Error actualizando el registro'})

@login_required
def delete_produccion(request, produccin_id):
    produccin = get_object_or_404(Produccin, pk=produccin_id, user=request.user)
    if request.method == 'POST':
        produccin.delete()
        return redirect('produccion')

@login_required
def searchp(request):
    busemp = request.GET["busemp"]
    produccins = Produccin.objects.filter(fecha__icontains=busemp)
    return render(request, 'produccin.html', {'produccins': produccins})

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('inventario')
