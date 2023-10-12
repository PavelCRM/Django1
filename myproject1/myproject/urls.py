from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
 path('client_ordered_products/<int:client_id>/', views.client_ordered_products, name='client_ordered_products'),
]