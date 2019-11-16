from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product


# Traz todos os produtos do banco de dados sem filtrar nada
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


def product_detail_view(request, pk=None, *args, **kwargs):
    print(args)
    print(kwargs)
    qs = Product.objects.filter(id=pk)
    if qs.exists():
        queryset = qs.first()
    else:
        raise Http404("Esse produto não existe!")

    context = {
        'object': queryset
    }
    return render(request, "products/detail.html", context)
