from django.shortcuts import render

from .models import Product


# Traz todos os produtos do banco de dados sem filtrar nada
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)
