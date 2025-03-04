from django.contrib import admin
from django.urls import path, include
from tables.views import table_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', table_list, name='home'),
    path('customers/', include('customers.urls')),
    path('tables/', include('tables.urls')),
    path('reservations/', include('reservations.urls')),
]
