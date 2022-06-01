from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('donacion.html', views.donacion, name='donacion'),
    path('Carrito.html', views.Carrito, name='Carrito'),
    path('Gato.html', views.Gato, name='Gato'),
    path('Perro.html', views.Perro, name='Perro'),
    path('tarjeta.html', views.tarjeta, name='tarjeta'),
    path('todos.html', views.todos, name='todos'),
    path('listar.html', views.listar, name='listar'), 
    path('modificar.html', views.modificar, name='modificar'), 
    path('agregar', views.agregar, name="agregar"),
    path('eliminarProducto /<idProducto>', views.eliminarProducto, name="eliminarProducto"),
    path('modificarProducto/<idProducto>', views.modificarProducto, name="modificarProducto"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)