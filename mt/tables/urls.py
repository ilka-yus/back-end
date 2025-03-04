from django.urls import path
from .views import table_list, table_create, table_available, table_detail, table_update

urlpatterns = [
    path('', table_list, name='table_list'),
    path('create/', table_create, name='table_create'),
    path('available/', table_available, name='table_available'),
    path('<int:id>/', table_detail, name='table_detail'),
    path('<int:id>/update/', table_update, name='table_update')
]