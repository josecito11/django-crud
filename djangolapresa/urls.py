"""djangolapresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from materiaprima import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('inventario/', views.inventario, name='inventario'),
    path('inventario/searchi/', views.searchi, name='searchi'),
    path('inventario/create/', views.create_inventario, name='inventario_create'),
    path('inventario/<int:inventario_id>/', views.inventario_detail, name='inventario_detail'),
    path('inventario/<int:inventario_id>/delete', views.delete_inventario, name='delete_inventario'),
    path('entrada/', views.entrada, name='entrada'),
    path('entrada/searche/', views.searche, name='searche'),
    path('entrada/create/', views.create_entrada, name='entrada_create'),
    path('entrada/<int:entrada_id>/', views.entrada_detail, name='entrada_detail'),
    path('entrada/<int:entrada_id>/delete', views.delete_entrada, name='delete_entrada'),
    path('salida/', views.salida, name='salida'),
    path('salida/searchs/', views.searchs, name='searchs'),
    path('salida/create/', views.create_salida, name='salida_create'),
    path('salida/<int:salida_id>/', views.salida_detail, name='salida_detail'),
    path('salida/<int:salida_id>/delete', views.delete_salida, name='delete_salida'),
    path('materiaprima/', views.Materiaprima, name='materiaprima'),
    path('materiaprima/search/', views.search, name='search'),
    path('materiaprima/create/', views.create_materiaprima, name='materiaprima_create'),
    path('materiaprima/<int:materiaprima_id>/', views.materiaprima_detail, name='materiaprima_detail'),
    path('materiaprima/<int:materiaprima_id>/delete', views.delete_materiaprima, name='delete_materiaprima'),
    path('materiaprima/<int:materiaprima_id>/delete', views.delete_materiaprima, name='delete_materiaprima'),
    path('produccion/', views.produccin, name='produccion'),
    path('produccion/searchp/', views.searchp, name='searchp'),
    path('produccion/create/', views.create_produccin, name='produccion_create'),
    path('produccion/<int:produccin_id>/', views.produccion_detail, name='produccion_detail'),
    path('produccion/<int:produccin_id>/delete', views.delete_produccion, name='delete_produccion'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin')
]
