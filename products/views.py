from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    # request = self.request
    # return Product.objects.featured()


def product_list_view(request):  # returns all database products without filtering anything
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


def product_detail_view(request, pk=None, *args, **kwargs):  # returns product by id database
    print(args)
    print(kwargs)
    qs = Product.objects.filter(id=pk)
    if qs.count() == 1:
        queryset = qs.first()
    else:
        raise Http404("Esse produto não existe!")

    context = {
        'object': queryset
    }
    return render(request, "products/detail.html", context)
