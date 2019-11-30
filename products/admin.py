from django.contrib import admin

from products.models import Product, CarouselImageHome


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug')

    class meta:
        model = Product


admin.site.register(Product, ProductAdmin)


@admin.register(CarouselImageHome)
class CarouselImageHomeAdmin(admin.ModelAdmin):
    class meta:
        model = CarouselImageHome
        extra = 1
