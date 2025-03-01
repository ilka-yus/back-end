from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_login, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/<int:id>/delete/', views.todo_delete, name='todo_delete'),
    path('todos/<int:id>/edit/', views.todo_edit, name='todo_edit'),
]
