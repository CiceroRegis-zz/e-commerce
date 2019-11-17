from django.urls import path

from products.views import ProductFeaturedListView, ProductFeaturedDetailView, product_detail_view
from .views import product_list_view, ProductDetailSlugView

urlpatterns = [
    path('products/', product_list_view),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view()),
]

