from django.shortcuts import render

# Create your views here.
#creamos la vista que se va a mostrar en el navegador
def productos_lista(request):
    #creamos una lista de productos dummy para mostrar en la vista
    #esta lista la podriamos traer de la base de datos
    lista_productos = [
        {'nombre': 'Producto 1', 'precio': 1000},
        {'nombre': 'Producto 2', 'precio': 2000},
        {'nombre': 'Producto 3', 'precio': 3000},
        {'nombre': 'Producto 4', 'precio': 4000},
        {'nombre': 'Producto 5', 'precio': 5000},
    ]
    #creamos un diccionario con la lista de productos en un contexto para pasarsela a la vista
    context = {
        'lista': lista_productos
    }
    #retornamos la vista con el contexto
    return render(request, 'productos_lista/productos_lista.html', context)