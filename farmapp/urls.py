from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from farmapp.views import (BusinessDeleteView, 
                          BusinessListView,
                          BusinessCreateView,
                          BusinessDetailView,
                          BusinessUpdateView,
                          PostCreateView,
                          PostDeleteView,
                          PostDetailView,
                          PostUpdateView,
                          PostListView,)


urlpatterns=[
    path('',BusinessListView.as_view(),name="home"),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('dashboard/', views.farmer_dashboard, name='dashboard'),
    # path('add_product/', views.add_product, name='add_product'),

    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('dashboard', views.dashboard, name='dashboard'),
    # path('post_product/', views.post_product, name='post_product'),
    # path('add_product_code/', views.add_product_code, name='add_product_code'),
    # path('add_product/', views.add_product, name='add_product'),
    
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('business/<int:pk>/',BusinessDetailView.as_view(),name='business-detail'),
    path('business/new/',BusinessCreateView.as_view(),name='business-create'),
    path('business/<int:pk>/update/',BusinessUpdateView.as_view(),name='business-update'),
    path('business/<int:pk>/delete/',BusinessDeleteView.as_view(),name='business-delete'),
    path('post/',PostListView.as_view(),name='post'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('search/',views.search_request,name='search_results'),
]