from django.urls import path
from .views import reservation_list, reservation_create, reservation_detail, reservation_list_by_user, reservation_update, reservation_delete

urlpatterns = [
    path('reservations/', reservation_list, name='reservation_list'),
    path('create/', reservation_create, name='reservation_create'),
    path('<int:id>/', reservation_detail, name='reservation_detail'),
    path('user/<int:user_id>/', reservation_list_by_user, name='reservation_list_by_user'),
    path('<int:id>/update/', reservation_update, name='reservation_update'),
    path('<int:id>/delete/', reservation_delete, name='reservation_delete'),
]