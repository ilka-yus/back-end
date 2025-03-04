from django.urls import path
from .views import customer_list, customer_create, customer_detail

urlpatterns = [
    path('customers/', customer_list, name='customer_list'),
    path('create/', customer_create, name='customer_create'),
    path('<int:id>/', customer_detail, name='customer_detail'),
]