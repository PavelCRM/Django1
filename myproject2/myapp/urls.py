from django.urls import path
from . import views

urlpatterns = [
    # URL-паттерны для клиентов
    path('create_client/', views.create_client, name='create_client'),
    path('view_clients/', views.view_clients, name='view_clients'),
    path('update_client/<int:client_id>/', views.update_client, name='update_client'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),

    # URL-паттерны для продуктов
    path('create_product/', views.create_product, name='create_product'),
    path('view_products/', views.view_products, name='view_products'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),

    # URL-паттерны для заказов
    path('create_order/', views.create_order, name='create_order'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('view_order/<int:order_id>/', views.view_order, name='view_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),

    path('client_ordered_products/<int:client_id>/<int:days>/', views.client_ordered_products, name='client_ordered_products'),
    
    # URL-паттерны изменения товара
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),

]