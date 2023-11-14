# from django.urls import path
# from . import views

# urlpatterns = [
#     path('products/', views.farm_product_list, name='farm_product_list'),
#     path('products/create/', views.farm_product_create, name='farm_product_create'),
#     path('products/<int:product_id>/buy/', views.buy_product, name='buy_product'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', views.post_product, name='post_product'),
    path('', views.view_requests, name='view_requests'),
    ]