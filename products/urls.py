from django.urls import path

from products.views import ProductFeaturedListView, ProductFeaturedDetailView, product_detail_view
from .views import product_list_view, ProductDetailSlugView

app_name = "products"
urlpatterns = [
    path('products/', product_list_view, name='list'),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail')
]
